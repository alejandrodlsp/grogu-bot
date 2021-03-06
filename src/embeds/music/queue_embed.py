import discord
import datetime as dt
from src.embeds.embed import Embed

EMBED_TITLE = "Queue"
EMBED_AUTHOR = "Query Results"
EMBED_FOOTER = "Requested by {}."
NEXT_UP_COLUMN = "Next up"
CURRENTLY_PLAYING_TAG="Currently Playing:"

class QueueEmbed(Embed):
    def __init__(self, ctx, queue, show):
        self.ctx = ctx
        self.embed = discord.Embed(
            title=EMBED_TITLE,
            description= f'Showing up to next {show} tracks out of **{queue.length}**',
            colour=ctx.author.colour,
            timestamp=dt.datetime.utcnow()
        )
        self.embed.set_author(name=EMBED_AUTHOR)
        self.embed.set_footer(
            text=EMBED_FOOTER.format(ctx.author.display_name), 
            icon_url=ctx.author.avatar_url
            )
        self.embed.add_field(
            name=CURRENTLY_PLAYING_TAG, 
            value = getattr(queue.current_track, "title", "No tracks currently playing"),
            inline=False
            )
        upcoming = queue.upcoming
        if upcoming:
            self.embed.add_field(
                name= NEXT_UP_COLUMN,
                value = "\n".join(str(i + queue.position + 1) + ") " + t.title for i, t in enumerate(upcoming[:show])),
                inline = False
            )
        