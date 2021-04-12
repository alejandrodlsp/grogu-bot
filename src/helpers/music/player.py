import asyncio
import discord
import wavelink

from discord.ext import commands

from src.embeds.music.choose_track_embed import ChooseTrackEmbed, ChooseTrackOptions
from src.helpers.music.queue import Queue, QueueIsEmptyError
from src.text import get_text

class AlreadyConnectedToChannelError(commands.CommandError):
    pass

class NoVoiceChannelError(commands.CommandError):
    pass

class NoTracksFoundError(commands.CommandError):
    pass

class QueryNotFoundError(commands.CommandError):
    pass

class Player(wavelink.Player):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queue = Queue()

    async def connect(self, ctx, channel = None):
        if self.is_connected:
            raise AlreadyConnectedToChannelError

        channel = getattr(ctx.author.voice, "channel", channel)
        if channel is None:
            raise NoVoiceChannelError

        await super().connect(channel.id)
        return channel

    async def teardown(self):
        try:
            await self.destroy()
        except KeyError:
            pass

    async def add_tracks(self, ctx, tracks, mode):
        if not tracks:
            raise NoTracksFoundError

        if isinstance(tracks, wavelink.TrackPlaylist):
            self.queue.add(*tracks.tracks)
        elif len(tracks) == 1:
            self.queue.add(tracks[0])
            await ctx.send(get_text('music_added_single_track_to_queue').format(tracks[0].title))
        else:
            if len(tracks) < 1:
                raise QueryNotFoundError

            track = tracks[0]
            if mode == 'c':
                track = await self.choose_track(ctx, tracks)
                
            if track is not None:
                self.queue.add(track)
                await ctx.send(get_text('music_added_single_track_to_queue').format(tracks[0].title))
        if not self.is_playing:
            await self.start_playback()
    
    async def choose_track(self, ctx, tracks):
        def _check(r, u):
            return (
                r.emoji in ChooseTrackOptions.keys()
                and u == ctx.author
                and r.message.id == msg.id
            )

        embed = ChooseTrackEmbed(ctx,tracks)
        msg = await embed.send()

        try:
            reaction, _ = await self.bot.wait_for("reaction_add", timeout=60.0, check=_check)
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.message.delete()
        else:
            await msg.delete()
            return tracks[ChooseTrackOptions[reaction.emoji]]

    async def start_playback(self):
        await self.play(self.queue.current_track)

    async def advance(self):
        try:
            track = self.queue.get_next_track()
            if track is not None:
                await self.play(track)
        except QueueIsEmptyError:
            pass