import discord
import datetime as dt
from src.embeds.embed import Embed

NUMBERS = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣")


class PollEmbed(Embed):
    def __init__(self, ctx, poll):
        self.ctx = ctx
        self.embed = discord.Embed(
            title="Poll",
            description=poll.question,
            colour=ctx.author.colour
        )

        fields = [
            ("Options", "\n".join(
                [f"{NUMBERS[idx]} - {option}" for idx, option in enumerate(poll.answers)]), False),
            ("Instructions", "Use pollstart to start poll; pollend to end the poll, or polladd **{option}** to add more options", False)]

        for name, value, inline in fields:
            self.embed.add_field(name=name, value=value, inline=inline)
