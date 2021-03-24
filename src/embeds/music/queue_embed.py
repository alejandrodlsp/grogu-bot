import discord
import datetime as dt

EMBED_TITLE = "Queue"
EMBED_AUTHOR = "Query Results"
EMBED_FOOTER = "Requested by {}"
NEXT_UP_COLUMN = "Next up"
CURRENTLY_PLAYING_TAG="Currently Playing:"

class QueueEmbed:
    def __init__(self, ctx, queue, show):
        self.ctx = ctx
        self.embed = discord.Embed(
            title=EMBED_TITLE,
            description= f'Showing up to next {show} tracks',
            colour=ctx.author.colour,
            timestamp=dt.datetime.utcnow()
        )
        self.embed.set_author(name=EMBED_AUTHOR)
        self.embed.set_footer(
            text=EMBED_FOOTER.format(ctx.author.display_name), 
            icon_url=ctx.author.avatar_url
            )
        self.embed.add_field(name=CURRENTLY_PLAYING_TAG, value = queue.current_track.title, inline=False)
        upcoming = queue.upcoming
        if upcoming:
            self.embed.add_field(
                name= NEXT_UP_COLUMN,
                value = "\n".join(t.title for t in upcoming[:show]),
                inline = False
            )

    async def send(self):
        self.msg = await self.ctx.send(embed=self.embed)
        return self.msg
        