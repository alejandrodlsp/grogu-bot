import discord
import datetime as dt
from src.embeds.embed import Embed

class HelpCommandEmbed(Embed):
    def __init__(self, ctx, command_name, description, params, aliases):
        self.ctx = ctx

        self.embed = discord.Embed(
            title = f"{command_name.capitalize()} command",
            description = aliases,
            colour = ctx.author.colour
        )

        self.embed.add_field(
            name = "Usage",
            inline= False,
            value = command_name + " " + params
        )

        self.embed.add_field(
            name = "Description",
            inline=False,
            value = description
        )
        
        self.embed.set_footer(
            icon_url=ctx.author.avatar_url
        )