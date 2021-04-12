import os
import discord
import logging
import datetime

try:
    os.makedirs('log')
    file = open('log/discord.log','a+')
    file.close()
except OSError as e:
    pass

logger = logging.getLogger('discord')

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='log/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def log_console(message, log_level = 1):
    timestamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

    if log_level == 1:
        info(message)
    elif log_level == 2:
        log(message)
    elif log_level == 3:
        log_warning(message)
    elif log_level == 4:
        log_error(message)

    print(f'{timestamp}> {message}')

def info(message):
    logger.info(message)
    
def log(message):
    logger.debug(message)

def log_warning(message):
    logger.warn(message)
    
def log_error(message):
    logger.error(message)