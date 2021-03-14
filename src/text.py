import json

global text_value
text_value = None

def load_text():
    with open('assets/text.json') as f:
        global text_value
        text_value = json.load(f)

def get_text(key):
    global text_value
    return text_value[key]