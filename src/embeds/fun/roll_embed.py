import discord
import datetime as dt
from src.embeds.embed import Embed

EMBED_TITLE = "Rolling number between **0** and **{}**"
EMBED_FOOTER = "Requested by {}"

class RollEmbed(Embed):
    def __init__(self, ctx, sides, number):
        self.ctx = ctx
        self.embed = discord.Embed(
            title=EMBED_TITLE.format(sides),
            colour=ctx.author.colour,
            timestamp=dt.datetime.utcnow()
        )
        self.embed.set_footer(
            text=EMBED_FOOTER.format(ctx.author.display_name), 
            icon_url=ctx.author.avatar_url
            )
        self.embed.add_field(name= "Roll: ", value = number, inline=False)
        