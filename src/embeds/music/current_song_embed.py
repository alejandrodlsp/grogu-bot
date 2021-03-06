import discord
import datetime as dt
from src.embeds.embed import Embed

EMBED_TITLE = "Currently playing:"
EMBED_FOOTER = "Requested by {}"

class CurrentSongEmbed(Embed):
    def __init__(self, ctx, queue):
        self.ctx = ctx
        self.embed = discord.Embed(
            title=EMBED_TITLE,
            colour=ctx.author.colour,
            timestamp=dt.datetime.utcnow()
        )
        self.embed.set_footer(
            text=EMBED_FOOTER.format(ctx.author.display_name), 
            icon_url=ctx.author.avatar_url
            )
        self.embed.add_field(name= "Name: ", value = queue.current_track.title, inline=False)
        