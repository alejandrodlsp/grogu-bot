import discord
import datetime as dt

EMBED_TITLE = "Choose a song"
EMBED_AUTHOR = "Query Results"
EMBED_FOOTER = "Invoked by {}"

ChooseTrackOptions = {
    "1️⃣": 0,
    "2⃣": 1,
    "3⃣": 2,
    "4⃣": 3,
    "5⃣": 4,
}

class ChooseTrackEmbed:
    def __init__(self, ctx, tracks):
        self.ctx = ctx
        self.tracks = tracks
        self.embed = discord.Embed(
            title=EMBED_TITLE,
            description=(
                "\n".join(
                    f"**{i+1}.** {t.title} ({t.length//60000}:{str(t.length%60).zfill(2)})"
                    for i, t in enumerate(tracks[:5])
                )
            ),
            colour=ctx.author.colour,
            timestamp=dt.datetime.utcnow()
        )
        self.embed.set_author(name=EMBED_AUTHOR)
        self.embed.set_footer(
            text=EMBED_FOOTER.format(ctx.author.display_name), 
            icon_url=ctx.author.avatar_url
            )
    
    async def send(self):
        self.msg = await self.ctx.send(embed=self.embed)

        for emoji in list(ChooseTrackOptions.keys())[:min(len(self.tracks), len(ChooseTrackOptions))]:
            await self.msg.add_reaction(emoji)

        return self.msg
        