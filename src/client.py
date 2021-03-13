import discord
from discord.ext import commands
import os
from src.logger import log

class Client:
    def __init__(self):
        COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")
        DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        client = commands.Bot(command_prefix=COMMAND_PREFIX)

        @client.event
        async def on_ready():
            log("Bot is ready")

        @client.event
        async def on_member_join(member):

        client.run(DISCORD_TOKEN)
