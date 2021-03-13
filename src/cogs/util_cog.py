import discord
from discord.ext import commands
from src.alias import get_aliases
from src.logger import log_console

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Util cog')

    @commands.command(aliases=get_aliases('ping'))
    async def ping(self, ctx):
        await ctx.send(f'Latency: {round(client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Util(client))