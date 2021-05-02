import discord
import random
import os

from typing import Optional
from urllib.parse import quote

from discord.ext.commands import cooldown, BucketType
from discord.ext import commands
from discord import Member

from src.alias import get_aliases
from src.logger import log_console
from src.text import get_text
from src.util import send_msg
from src.embeds.fun.roll_embed import RollEmbed
from src.helpers.api_handler import request_text, request_image, request_canvas_image

CD_RATE = int(os.getenv("HTTP_CD_RATE"))
CR_DURATION = int(os.getenv("HTTP_CD_DURATION"))


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Fun cog')

    @commands.command(name='dice', aliases=get_aliases('dice'))
    async def dice_command(self, ctx, sides=6):
        """
        Rolls a dice
        """

        embed = RollEmbed(ctx, sides, random.randint(0, sides))
        await embed.send()

    @commands.command(name='slap', aliases=get_aliases('slap'))
    async def slap_command(self, ctx, member: Member, *, reason: Optional[str] = "no reason"):
        """
        Slap a member
        """

        await send_msg(ctx, "fun_slap_command_message", ctx.author.name, member.mention, reason)

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="dog", aliases=get_aliases("dog"))
    async def dog_command(self, ctx):
        """
        Gives you a random dog picture
        """

        await request_image(ctx, "https://some-random-api.ml/img/dog", title="Requested dog image", description="Here is your doggo :)")

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="wink", aliases=get_aliases("wink"))
    async def wink_command(self, ctx):
        """
        Winks at you
        """

        await request_image(ctx, "https://some-random-api.ml/animu/wink", title=":wink:")

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="pat", aliases=get_aliases("pat"))
    async def pat_command(self, ctx):
        """
        Get a pat in the back
        """

        await request_image(ctx, "https://some-random-api.ml/animu/pat", title=":hand_splayed:")

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="hug", aliases=get_aliases("hug"))
    async def hug_command(self, ctx):
        """
        If you need a hug
        """

        await request_image(ctx, "https://some-random-api.ml/animu/hug", title=":hugging:")

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="gay", aliases=get_aliases("gay"))
    async def gay_command(self, ctx, member: discord.Member = None):
        """
        Gay overlay for avatar
        """

        if not member:
            member = ctx.author
        await request_canvas_image(ctx, "https://some-random-api.ml/canvas/gay", member)

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="glass", aliases=get_aliases("glass"))
    async def glass_command(self, ctx, member: discord.Member = None):
        """
        Glass overlay for avatar
        """

        if not member:
            member = ctx.author
        await request_canvas_image(ctx, "https://some-random-api.ml/canvas/glass", member)

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="wasted", aliases=get_aliases("wasted"))
    async def wasted_command(self, ctx, member: discord.Member = None):
        """
        Classic GTA Wasted overlay for avatar
        """

        if not member:
            member = ctx.author
        await request_canvas_image(ctx, "https://some-random-api.ml/canvas/wasted", member)

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="triggered", aliases=get_aliases("triggered"))
    async def triggered_command(self, ctx, member: discord.Member = None):
        """
        Triggered overlay for avatar
        """

        if not member:
            member = ctx.author
        await request_canvas_image(ctx, "https://some-random-api.ml/canvas/triggered", member, is_gif=True)

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="invert", aliases=get_aliases("invert"))
    async def invert_command(self, ctx, member: discord.Member = None):
        """
        Invert avatar image
        """

        if not member:
            member = ctx.author
        await request_canvas_image(ctx, "https://some-random-api.ml/canvas/invert", member)

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="youtube", aliases=get_aliases("youtube"))
    async def youtube_command(self, ctx, member: discord.Member, username, *, comment):
        """
        Generate a fake youtube comment
        """

        await request_canvas_image(
            ctx,
            "https://some-random-api.ml/canvas/youtube-comment",
            member,
            params={"username": username, "comment": comment}
        )

    @cooldown(CD_RATE, CR_DURATION, BucketType.guild)
    @commands.command(name="meme", aliases=get_aliases("meme"))
    async def meme_command(self, ctx):
        """
        Shows you a random meme
        """

        await request_image(ctx, "https://some-random-api.ml/meme", key="image", title="Here's your meme")


def setup(client):
    client.add_cog(Fun(client))
