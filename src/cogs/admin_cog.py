import discord
from discord.ext import commands
from src.alias import get_aliases
from src.logger import log_console

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Admin cog')

def setup(client):
    client.add_cog(Admin(client))