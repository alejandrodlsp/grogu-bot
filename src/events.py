import os
import discord
from discord.ext import commands
from src.util import send_msg
from src.logger import log, log_console
from src.client import client
from src.prefix import create_prefix_entry, remove_prefix_entry

log_console("Registering events...")

@client.event
async def on_ready():
    log('Bot serving in as {0.user}'.format(client))

    log_console("Starting tasks...")
    import src.tasks
    src.tasks.start()

@client.event
async def on_member_join(member):
    log(f'{member.name}#{member.id} ({member.nick}) has joined the sever: {member.guild}.')

@client.event
async def on_member_remove(member):
    log(f'{member.name}#{member.id} ({member.nick}) has left the sever: {member.guild}.')

@client.event
async def on_command_error(ctx, error):
    if(isinstance(error, commands.CommandNotFound)):
        await send_msg(ctx, 'command_not_found_error')

@client.event
async def on_guild_join(guild):
    create_prefix_entry(guild)
    
@client.event
async def on_guild_remove(guild):
    remove_prefix_entry(guild)
