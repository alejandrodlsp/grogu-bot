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

    @commands.command(name='kick', aliases=get_aliases('kick'))
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, ctx, member : discord.Member, *, reason=None):
        member_name, member_discriminator = member.split('#')

        log(f'User kick: {ctx.author.name}#{ctx.author.id} kicked {member_name}#{member_discriminator} in {ctx.guild} for reason: {reason}')
        await member.kick(reason=reason)
        await ctx.send(get_text("user_kick").format(member_name, member_discriminator))

    @kick_command.error
    async def kick_command_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .kick *user*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

    @commands.command(name='ban', aliases=get_aliases('ban'))
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, ctx, member : discord.Member, *, reason=None):
        member_name, member_discriminator = member.split('#')

        log(f'User ban: {ctx.author.name}#{ctx.author.id} banned {member_name}#{member_discriminator} in {ctx.guild} for reason: {reason}')
        await member.ban(reason=reason)
        await ctx.send(get_text("user_ban").format(member_name, member_discriminator))

    @ban_command.error
    async def ban_command_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .ban *user*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

    @commands.command(name='unban', aliases=get_aliases('unban'))
    @commands.has_permissions(administrator=True)
    async def unban_command(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member.name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(get_text("user_pardon").format(member_name, member_discriminator))
                log(f'User pardon: {ctx.author.name}#{ctx.author.id} unbaned {member_name}#{member_discriminator} in {ctx.guild}')

    @unban_command.error
    async def unban_command_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .unban *user*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

    @commands.command(name='changeprefix', aliases=get_aliases('changeprefix'))
    @commands.has_permissions(administrator=True)
    async def changeprefix_command(self, ctx, prefix):
        change_prefix(ctx, prefix)

    @changeprefix_command.error
    async def changeprefix_command_error(self, ctx, error):
        if(isinstance(error, commands.MissingRequiredArgument)):
            await ctx.send("Missing arguments: .changeprefix *prefix*")
        if(isinstance(error, commands.MissingPermissions)):
            await ctx.send(get_text("unsufficient_permissions"))

def setup(client):
    client.add_cog(Admin(client))