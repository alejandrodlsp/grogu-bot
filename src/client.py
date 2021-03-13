import discord
from discord.ext import commands
import os
from src.logger import log

class Client:
    def __init__(self, name):
        COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")
        self.bot = commands.Bot(command_prefix=COMMAND_PREFIX)

        @client.event
        async def on_ready():
            log("Bot is ready")
        