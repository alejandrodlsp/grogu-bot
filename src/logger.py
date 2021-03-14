import discord
import logging
import datetime

logger = logging.getLogger('discord')

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='log/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def log_console(message, log_level = 1):
    timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    print(f'{timestamp}> {message}')

    if log_level == 1:
        log(message)
    elif log_level == 2:
        log_warning(message)
    elif log_level == 3:
        log_error(message)

def log(message):
    logger.debug(message)

def log_warning(message):
    logger.warn(message)
    
def log_error(message):
    logger.error(message)