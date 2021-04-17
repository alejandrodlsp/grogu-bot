import discord
import datetime as dt
from src.embeds.embed import Embed

class ImageEmbed(Embed):
    def __init__(self, ctx, title, description, footer, image_link):
        self.ctx = ctx
        self.embed = discord.Embed(
            title=title,
            description=description,
            colour=ctx.author.colour,
            timestamp=dt.datetime.utcnow()
        )
        self.embed.set_footer(
            text=footer, 
            icon_url=ctx.author.avatar_url
            )
        self.embed.set_image(url=image_link)
        