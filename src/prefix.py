import os
import json

PREFIXES_FILE_PATH = 'db/prefixes.json'
COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")

def get_prefix(client, message):
    with open(PREFIXES_FILE_PATH, 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

def create_prefix_entry(guild):
    with open(PREFIXES_FILE_PATH, 'r') as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = COMMAND_PREFIX
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
