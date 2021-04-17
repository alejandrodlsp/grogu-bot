import discord
from discord import Embed
from src.embeds.help.help_command_embed import HelpCommandEmbed
from src.embeds.help.help_embed import HelpMenuEmbed
from discord.ext.menus import MenuPages


def params(command):
    params = []
    for key, value in command.params.items():
        if key not in ("self", "ctx"):
            params.append(f"[{key}]" if "NoneType" in str(
                value) else f"<{key}>")
    params = " ".join(params)
    return params


def cmd_and_aliases(command):
    return " | ".join([str(command), *command.aliases])


def cmd_description(command):
    return cmd_and_aliases(command) + " " + params(command)


async def show_command_help(ctx, command):
    embed = HelpCommandEmbed(ctx, str(command), command.help, params(
        command), cmd_and_aliases(command))
    await embed.send()


async def show_commands_help(ctx, commands):
    menu = MenuPages(
        source=HelpMenuEmbed(ctx, list(commands), cmd_description),
        clear_reactions_after=True,
        delete_message_after=True,
        timeout=120.0
    )

    await menu.start(ctx)
