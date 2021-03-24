import os
import discord
from discord.ext import commands
from src.logger import log_console
from src.prefix import get_prefix

global client
client = None

class Client(commands.Bot):
    def __init__(self):
        log_console("Initializing bot client...", 1)

        super().__init__(
            command_prefix=get_prefix, 
            case_insensitive=True, 
            intents=discord.Intents.all()
            )

        global client
        client = self

    def setup(self):
        log_console("Running setup...", 1)

        import src.events

        log_console("Loading cogs...", 1)
        for filename in os.listdir('./src/cogs'):
            if filename.endswith('_cog.py'):
                cog_name = filename[:-3]
                if not (cog_name == 'music_cog'):
                    self.load_extension(f'src.cogs.{cog_name}')

    def run(self):
        self.setup()

        DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        super().run(DISCORD_TOKEN, reconnect=True)

    async def shutdown(self):
        log_console('Shutting down...', 1)
        await super().close()

    async def close(self):
        log_console('Closing on keyboard interrupt...', 1)
        await self.shutdown()

    async def on_connect(self):
        log_console(f'Connected to Discord (latency {self.latency * 1000:,.0f}ms).', 1)
    
    async def on_resume(self):
        log_console('Bot resumed.', 2)

    async def on_disconnect(self):
        log_console('Bot disconnected.', 2)

    async def on_ready(self):
        self.client_id = (await self.application_info()).id
        log_console('Bot ready', 1)

    #async def prefix(self, bot, msg):
    #    return commands.when_mentioned_or('.')(bot, msg)

    async def process_commands(self, msg):
        ctx = await self.get_context(msg, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    async def on_message(self, msg):
        if not msg.author.bot:
            await self.process_commands(msg)
    