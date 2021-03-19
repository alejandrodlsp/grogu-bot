import os
import re
import typing as t
import datetime as dt

import discord
import wavelink

from discord.ext import commands

from src.helpers.music.player import Player
from src.embeds.music.queue_embed import QueueEmbed

from src.alias import get_aliases
from src.logger import log_console
from src.text import get_text

URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
 
class Music(commands.Cog, wavelink.WavelinkMixin):
    def __init__(self, bot):
        self.bot = bot
        self.wavelink = wavelink.Client(bot=bot)
        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()
        node = {
            "host": os.getenv("LAVALINK_SERVER_ADDRESS"),
            "port": os.getenv("LAVALINK_SERVER_PORT"),
            "rest_uri": f'http://{os.getenv("LAVALINK_SERVER_ADDRESS")}:{os.getenv("LAVALINK_SERVER_PORT")}',
            "password": os.getenv("LAVALINK_SERVER_PASSWORD"),
            "identifier": "MAIN",
            "region": os.getenv("LAVALINK_SERVER_REGION")
        }
        await self.wavelink.initiate_node(**node)

    def get_player(self, obj):
        if isinstance(obj, commands.Context):
            return self.wavelink.get_player(obj.guild.id, cls=Player, context=obj)
        elif isinstance(obj, discord.Guild):
            return self.wavelink.get_player(obj.id, cls=Player)

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Music cog')

    @wavelink.WavelinkMixin.listener()
    async def on_node_ready(self, node):
        log_console(f'Wavelink node {node.identifier} ready', 1)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not member.bot and after.channel is None:
            if not [m for m in before.channel.members if not m.bot]:
                await self.get_player(member.guild).teardown()

    @wavelink.WavelinkMixin.listener("on_track_stuck")
    @wavelink.WavelinkMixin.listener("on_track_end")
    @wavelink.WavelinkMixin.listener("on_track_exception")
    async def on_player_stop(self, node, payload):
        await payload.player.advance()

    async def cog_check(self, ctx):
        if isinstance(ctx.channel, discord.DMChannel):
            await ctx.send(get_text("music_no_available_on_dm_error"))
            return False
        return True

    @commands.command(name='connect', aliases=get_aliases('connect'))
    async def connect_command(self, ctx, *, channel: t.Optional[discord.VoiceChannel]):
        player = self.get_player(ctx)
        channel = await player.connect(ctx, channel)
        await ctx.send(get_text("music_channel_on_connect").format(channel.name))

    @connect_command.error
    async def connect_command_error(self, ctx, error):
        if isinstance(error, AlreadyConnectedToChannel):
            await ctx.send(get_text("music_already_connected_to_channel_error"))
        elif isinstance(error, NoVoiceChannel):
            await ctx.send(get_text("music_no_voice_channel_error"))
    
    @commands.command(name='queue', aliases=get_aliases('queue'))
    async def queue_command(self, ctx, show : t.Optional[int] = 10):
        player = self.get_player(ctx)
        if player.queue.is_empty:
            raise QueueIsEmpty
            
        embed = QueueEmbed(ctx, player.queue, show)
        msg = await embed.send()

    @queue_command.error
    async def queue_command_error(self, ctx, error):
        if isinstance(error, QueueIsEmpty):
            await ctx.send(get_text("music_queue_is_empty_error"))

    @commands.command(name='disconnect', aliases=get_aliases('disconnect'))
    async def disconnect_command(self, ctx):
        player = self.get_player(ctx)
        await player.teardown()
        await ctx.send(get_text("music_channel_on_disconnect"))

    @disconnect_command.error
    async def disconnect_command_error(self, ctx, error):
        pass

    @commands.command(name='play', aliases=get_aliases('play'))
    async def play_command(self, ctx, *, query: t.Optional[str]):
        player = self.get_player(ctx)

        if not player.is_connected:
            await player.connect(ctx)
        
        if query is None:
            pass

        else:
            query = query.strip("<>")
            if not re.match(URL_REGEX, query):
                query = f"ytsearch:{query}"

            await player.add_tracks(ctx, await self.wavelink.get_tracks(query))


def setup(client):
    client.add_cog(Music(client))