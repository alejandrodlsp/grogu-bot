import discord
from typing import Optional
from discord.ext import commands
from src.logger import log_console
from src.alias import get_aliases
from src.helpers.log.log_helper import get_member_log_channel, set_member_log_channel
from src.helpers.log.log_helper import get_message_log_channel, set_message_log_channel
from src.embeds.log.member_update_embed import MemberUpdateNickEmbed, MemberUpdateRolesEmbed
from src.embeds.log.message_edit_embed import MessageEditEmbed, MessageDeletedEmbed


class Log(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Log cog')

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        log_channel = get_member_log_channel(self.client, after.guild.id)
        if log_channel is None:
            return

        if before.display_name != after.display_name:
            embed = MemberUpdateNickEmbed(log_channel, before, after)
            await embed.send()
        elif before.roles != after.roles:
            embed = MemberUpdateRolesEmbed(log_channel, before, after)
            await embed.send()

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if after.author.bot or after.guild is None:
            return

        log_channel = get_message_log_channel(self.client, after.guild.id)
        if log_channel is None:
            return

        if before.content != after.content:
            embed = MessageEditEmbed(log_channel, before, after)
            await embed.send()

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot or message.guild is None:
            return

        log_channel = get_message_log_channel(self.client, message.guild.id)
        if log_channel is None:
            return

        embed = MessageDeletedEmbed(log_channel, message)
        await embed.send()

    @commands.command(name="memberlog", aliases=get_aliases("memberlog"))
    @commands.has_permissions(manage_guild=True)
    async def memberlog_command(self, ctx, channel: Optional[discord.TextChannel]):
        """
        Sets the default text channel to log member update events.
        """

        if channel is not None:
            channel_id = channel.id
        else:
            channel_id = 0
        set_member_log_channel(self.client, ctx.guild.id, channel_id)
        channel_name = "  # " + channel.name if channel_id != 0 else "none"
        await ctx.send(f"Memberlog channel was changed to {channel_name}")

    @commands.command(name="messagelog", aliases=get_aliases("messagelog"))
    @commands.has_permissions(manage_guild=True)
    async def messagelog_command(self, ctx, channel: Optional[discord.TextChannel]):
        """
        Sets the default text channel to log message update events.
        """

        if channel is not None:
            channel_id = channel.id
        else:
            channel_id = 0
        set_message_log_channel(self.client, ctx.guild.id, channel_id)
        channel_name = "  # " + channel.name if channel_id != 0 else "none"
        await ctx.send(f"Messagelog channel was changed to {channel_name}")


def setup(client):
    client.add_cog(Log(client))
