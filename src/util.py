import os
import asyncio

delay = float(os.getenv("DELAYED_MESSAGE_DURATION"))

async def delayed_message(ctx, message, delay=delay):
    message = await ctx.send(message)
    await asyncio.sleep(delay) 
    await message.delete()