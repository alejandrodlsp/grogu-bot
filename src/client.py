import os
import discord
from discord.ext import commands
from src.logger import log_console
from src.prefix import get_prefix

global client
client = None

class Client:
    def __init__(self):
        DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        
        log_console("Initializing bot client...")
        global client
        client = commands.Bot(command_prefix=get_prefix)
        
        log_console("Registering events...")
        import src.events

        log_console("Loading cogs...")
        for filename in os.listdir('./src/cogs'):
            if filename.endswith('_cog.py'):
                cog_name = filename[:-3]
                client.load_extension(f'src.cogs.{cog_name}')

        log_console("Executing bot client...")
        client.run(DISCORD_TOKEN)