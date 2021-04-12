import json

global __text
__text = None

def load_text():
    with open('assets/text.json') as f:
        global __text
        __text = json.load(f)

def get_text(key):
    global __text
    return __text[key]