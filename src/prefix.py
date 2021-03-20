import os
import json

PREFIXES_FILE_PATH = 'db/prefixes.json'

def get_prefix(client, message):
    with open(PREFIXES_FILE_PATH, 'r') as f:
        prefixes = json.load(f)
    if (prefix := prefixes[str(message.guild.id)]) is None:
        create_prefix_entry(client.guild)
    return prefix

def create_prefix_entry(guild):
    with open(PREFIXES_FILE_PATH, 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = os.getenv("COMMAND_PREFIX")
    with open(PREFIXES_FILE_PATH, 'w') as f:
        json.dump(prefixes, f, indent = 4)

def remove_prefix_entry(guild):
    with open(PREFIXES_FILE_PATH, 'r') as f:
        prefixes = json.load(f)
    prefixes.pop(str(guild.id))
    with open(PREFIXES_FILE_PATH, 'w') as f:
        json.dump(prefixes, f, indent = 4)

def change_prefix(ctx, prefix):
    with open(PREFIXES_FILE_PATH, 'r') as f:
        prefixes = json.load(f)
    prefixes[str(ctx.guild.id)] = prefix
    with open(PREFIXES_FILE_PATH, 'w') as f:
        json.dump(prefixes, f, indent = 4)
