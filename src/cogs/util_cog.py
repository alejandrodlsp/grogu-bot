import discord
from discord.ext import commands
from src.alias import get_aliases
from src.logger import log_console
from src.text import get_text
from src.util import delayed_message

class Util(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Util cog')

    @commands.command(name='ping', liases=get_aliases('ping'))
    async def ping_command(self, ctx):
        await ctx.send(f'Latency: {round(client.latency * 1000)}ms')

    @commands.command(name='clear', aliases=get_aliases('clear'))
    @commands.has_permissions(manage_messages=True)
    async def clear_command(self, ctx, amount=5):
        await ctx.channel.purge(limit = amount)
        await delayed_message(ctx, get_text("message_cleared").format(amount), 3)

    @clear_command.error
    async def clear_command_error(self, ctx, error):
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

def setup(client):
    client.add_cog(Util(client))