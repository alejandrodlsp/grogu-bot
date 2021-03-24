import os
import discord
from itertools import cycle
from discord.ext import tasks
from src.client import client

PRESENCE = cycle(os.getenv("PRESENCE").split(','))
PRESENCE_CYCLE_DURATION = float(os.getenv("PRESENCE_CYCLE_DURATION"))

@tasks.loop(seconds=PRESENCE_CYCLE_DURATION)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(PRESENCE)))

def start():
    change_status.start()