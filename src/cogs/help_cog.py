import discord
from typing import Optional
from discord.ext import commands
from discord.utils import get
from src.alias import get_aliases
from src.logger import log_console
from src.helpers.help.help_helper import show_command_help, show_commands_help
from src.client import client


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Help cog')

    @commands.command(name="help", aliases=get_aliases("help"))
    async def help_command(self, ctx, cmd: Optional[str]):
        """
        Shows this help message.
        """

        if cmd is None:
            global client
            await show_commands_help(ctx, client.commands)
        else:
            command = get(self.client.commands, name=cmd)
            if command is not None:
                await show_command_help(ctx, command)
            else:
                send_msg(ctx, "command_not_found_error")


def setup(client):
    client.add_cog(Help(client))
