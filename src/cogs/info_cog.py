import discord
from discord.ext import commands
from typing import Optional
from src.alias import get_aliases
from src.logger import log_console
from src.text import get_text
from src.util import delayed_message, send_msg
from src.embeds.info.info_embed import UserInfoEmbed, GuildInfoEmbed


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Info cog')

    @commands.command(name="userinfo", aliases=get_aliases("userinfo"))
    async def userinfo_command(self, ctx, target: Optional[discord.Member]):
        target = target or ctx.author

        embed = UserInfoEmbed(ctx, target)
        await embed.send()

    @commands.command(name="serverinfo", aliases=get_aliases("serverinfo"))
    async def serverinfo_command(self, ctx):
        embed = GuildInfoEmbed(ctx)
        await embed.send()


def setup(client):
    client.add_cog(Info(client))
