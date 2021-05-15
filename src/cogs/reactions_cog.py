from asyncio.windows_events import NULL
import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
from src.alias import get_aliases
from src.logger import log_console
from src.text import get_text
from src.util import send_msg
from discord.embeds import Embed
from datetime import date, datetime, timedelta
from src.embeds.reactions.poll_embed import PollEmbed
from statistics import mode

NUMBERS = ("1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣")


class Poll:
    def __init__(self, question, answers, message=0, channel_id=0):
        self.message = message
        self.channel_id = channel_id
        self.question = question
        self.answers = answers

    @property
    def answers_count(self):
        return len(self.answers)

    def add_answer(self, answer):
        self.answers.append(answer)

    async def add_reactions(self):
        for emoji in NUMBERS[:len(self.answers)]:
            await self.message.add_reaction(emoji)


class Reactions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.polls = []

    async def get_poll(self, ctx, channel_id):
        for pl in self.polls:
            if pl.channel_id == ctx.channel.id:
                return pl
        await send_msg(ctx, "poll_add_error")
        return None

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Reactions cog')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message = await self.client.get_channel(payload.channel_id).fetch_message(payload.message_id)
        poll = await self.get_poll(message, payload.channel_id)
        if not poll:
            return

        for reaction in message.reactions:
            if not payload.member.bot:
                if (payload.member in await reaction.users().flatten() and reaction.emoji != payload.emoji.name):
                    await message.remove_reaction(reaction, payload.member)

    @commands.command(name="poll", aliases=get_aliases("poll"))
    async def poll_command(self, ctx, question: str, *options):
        """
        Creates a new poll for the current text channel with a question and a set of option strings
        """

        if (ctx.channel.id in (poll.channel_id for poll in self.polls)):
            await send_msg(ctx, "poll_already_exist_error")
            return

        if len(options) > 9:
            await send_msg(ctx, "poll_max_answers_error")
            return

        await ctx.message.delete()

        poll = Poll(question, [*options])
        embed = PollEmbed(ctx, poll)
        message = await ctx.send(embed=embed.embed)

        poll.message = message
        poll.channel_id = message.channel.id

        self.polls.append(poll)

    @commands.command(name="polladd", aliases=get_aliases("polladd"))
    async def polladd_command(self, ctx, *, option: str):
        """
        Adds an option to the currently active poll
        """

        poll = await self.get_poll(ctx, ctx.channel.id)
        if not poll:
            return

        await ctx.message.delete()
        poll.add_answer(option)

        embed = PollEmbed(ctx, poll)
        await poll.message.delete()
        message = await ctx.send(embed=embed.embed)
        poll.message = message

    @commands.command(name="pollstart", aliases=get_aliases("pollstart"))
    async def pollstart_command(self, ctx, minutes: int = None):
        """
        Starts the currently active poll; with a time in minutes (Max 15) (Optional)
        """

        poll = await self.get_poll(ctx, ctx.channel.id)
        if not poll:
            await send_msg(ctx, "poll_remove_error")
            return

        await ctx.message.delete()
        await poll.add_reactions()

        if minutes != None:
            minutes = min(minutes, 15)
            self.client.scheduler.add_job(
                self.complete_poll, "date", run_date=datetime.now()+timedelta(minutes=minutes), args=[poll])

    @pollstart_command.error
    async def pollstart_command_error(self, ctx, err):
        if isinstance(err, commands.MissingRequiredArgument):
            ctx.send("Missing required argument, use: pollstart {minutes}")

    @commands.command(name="pollstop", aliases=get_aliases("pollstop"))
    async def pollstop_command(self, ctx):
        """
        Stops the currently active poll and gives results
        """

        poll = await self.get_poll(ctx, ctx.channel.id)
        if not poll:
            await send_msg(ctx, "poll_remove_error")
            return

        await self.complete_poll(poll)

    @commands.command(name="pollremove", aliases=get_aliases("pollremove"))
    async def pollremove_command(self, ctx):
        """
        Deletes the currently active poll if not started.
        """

        poll = await self.get_poll(ctx, ctx.channel.id)
        if not poll:
            await send_msg(ctx, "poll_remove_error")
            return
        poll.message.delete()
        self.polls.remove(poll)

    async def complete_poll(self, poll):
        message = await self.client.get_channel(poll.channel_id).fetch_message(poll.message.id)

        most_voted = max(message.reactions, key=lambda r: r.count)

        emoji_index = NUMBERS.index(most_voted.emoji)
        await message.channel.send(get_text("poll_finish_results").format(most_voted.emoji, most_voted.count-1, poll.answers[emoji_index]))

        self.polls.remove(poll)


def setup(client):
    client.add_cog(Reactions(client))
