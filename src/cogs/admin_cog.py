import discord
from discord.ext import commands
from src.alias import get_aliases
from src.logger import log_console, log
from src.text import get_text
from src.prefix import change_prefix

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log_console(f'\tLoaded Admin cog')

    @commands.command(aliases=get_aliases('kick'))
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        log(f'User kick: {ctx.author.name}#{ctx.author.id} kicked {member.name}#{member.id} in {ctx.guild} for reason: {reason}')
        await member.kick(reason=reason)

    @kick.error
    async def kick_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .kick *user*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

    @commands.command(aliases=get_aliases('ban'))
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        log(f'User ban: {ctx.author.name}#{ctx.author.id} banned {member.name}#{member.id} in {ctx.guild} for reason: {reason}')
        await member.ban(reason=reason)

    @ban.error
    async def ban_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .ban *user*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

    @commands.command(aliases=get_aliases('unban'))
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(get_text("user_pardon").format(member_name, member_discriminator))
                log(f'User pardon: {ctx.author.name}#{ctx.author.id} unbaned {member_name}#{member_discriminator} in {ctx.guild}')

    @unban.error
    async def unban_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .unban *user*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

    @commands.command(aliases=get_aliases('changeprefix'))
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        change_prefix(ctx, prefix)

    @changeprefix.error
    async def changeprefix_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .changeprefix *prefix*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

def setup(client):
    client.add_cog(Admin(client))