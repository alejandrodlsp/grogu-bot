import os
import json
from discord.ext.commands import when_mentioned_or
from src.db import db

PREFIXES_FILE_PATH = 'db/prefixes.json'


def get_prefix(client, message):
    prefix = db.field(
        "SELECT prefix FROM guilds WHERE guild_id = ?;",
        message.guild.id
    )
    if prefix is None:
        create_entry(message.guild.id)
        return get_prefix(client, message)

    return when_mentioned_or(prefix)(client, message)


def change_prefix(ctx, prefix):
    db.execute(
        "UPDATE Guilds SET prefix = ? WHERE guild_id = ?;",
        prefix, ctx.guild.id
    )


def create_entry(guild_id):
    db.execute(
        "INSERT INTO Guilds (guild_id, prefix) VALUES (?, ?);",
        guild_id,
        os.getenv("COMMAND_PREFIX")
    )
