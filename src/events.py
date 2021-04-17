import os
import discord
from discord.ext import commands
from src.util import send_msg
from src.logger import log, log_console
from src.client import client
from src.prefix import create_entry, remove_entry

log_console("Registering events...")


@client.event
async def on_ready():
    log('Bot serving in as {0.user}'.format(client))

    log_console("Starting jobs...")
    import src.jobs
    src.jobs.start()


@client.event
async def on_member_join(member):
    db.execute(
        "INSERT INTO experience (user_id) VALUES (?)",
        member.id
    )


@client.event
async def on_member_leave(member):
    db.execute(
        "DELETE FROM experience WHERE user_id = ?;",
        member.id
    )


@client.event
async def on_guild_join(guild):
    create_entry(guild.id)


@client.event
async def on_guild_remove(guild):
    remove_entry(guild.id)
