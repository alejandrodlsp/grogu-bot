import discord
import datetime as dt
from src.embeds.embed import Embed


class UserInfoEmbed(Embed):
    def __init__(self, ctx, target):
        self.ctx = ctx
        self.embed = discord.Embed(
            title="User information",
            colour=target.colour,
            timestamp=dt.datetime.utcnow()
        )
        self.embed.set_thumbnail(url=target.avatar_url)

        fields = [
            ("Name", str(target), True),
            ("ID", target.id, False),
            ("Bot?", target.bot, True),
            ("Role", target.top_role.mention, True),
            ("Status", str(target.status).title(), True),
            ("Created at", target.created_at.strftime(
                "%d/%m/%Y at %H:%M:%S"), True),
            ("Joined at", target.joined_at.strftime("%d/%m/%Y at %H:%M:%S"), True),
        ]

        for name, value, inline in fields:
            self.embed.add_field(name=name, value=value, inline=inline)


class GuildInfoEmbed(Embed):
    def __init__(self, ctx):
        self.ctx = ctx
        self.embed = discord.Embed(
            title="Server information",
            colour=ctx.guild.owner.colour,
            timestamp=dt.datetime.utcnow()
        )

        fields = [
            ("ID", ctx.guild.id, True),
            ("Owner", ctx.guild.owner.mention, True),
            ("Region", ctx.guild.region, True),
            ("Created at", ctx.guild.created_at.strftime(
                "%d/%m/%Y at %H:%M:%S"), True),
            ("Members", len(ctx.guild.members), True),
            ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
            ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
            ("Text channels", len(ctx.guild.text_channels), True),
            ("Voice channels", len(ctx.guild.voice_channels), True),
            ("Categories", len(ctx.guild.categories), True),
            ("Roles", len(ctx.guild.roles), True),
            ("\u200b", "\u200b", True),
        ]

        for name, value, inline in fields:
            self.embed.add_field(name=name, value=value, inline=inline)
