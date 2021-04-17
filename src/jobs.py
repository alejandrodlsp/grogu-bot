import os
import discord
from itertools import cycle
from src.client import client
from apscheduler.triggers.cron import CronTrigger

PRESENCE = cycle(os.getenv("PRESENCE").split(','))

async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(next(PRESENCE)))

def start():
    client.scheduler.add_job(change_status, CronTrigger(minute="0,10,20,30,40,50"))
    client.scheduler.start()