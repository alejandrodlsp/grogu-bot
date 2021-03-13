from src.logger import log
from discord.ext import commands
from src.client import client

@client.event
async def on_ready():
    log('Bot serving in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    log(f'{member.name}#{member.id} ({member.nick}) has joined the sever: {member.guild}.')

@client.event
async def on_member_remove(member):
    log(f'{member.name}#{member.id} ({member.nick}) has left the sever: {member.guild}.')
