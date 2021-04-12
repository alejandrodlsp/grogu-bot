import json

global __aliases
__aliases = None

def load_aliases():
    with open('assets/alias.json') as f:
        global __aliases
        __aliases = json.load(f)

def get_aliases(command):
    global __aliases
    return __aliases[command] if command in __aliases else []