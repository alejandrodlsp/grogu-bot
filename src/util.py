import os
import asyncio
from src.text import get_text

delay = float(os.getenv("DELAYED_MESSAGE_DURATION"))

async def delayed_message(ctx, message, delay=delay):
    message = await ctx.send(message)
    await asyncio.sleep(delay) 
    await message.delete()

async def send_msg(ctx, message, *params):
    await ctx.send(get_text(message).format(*params))