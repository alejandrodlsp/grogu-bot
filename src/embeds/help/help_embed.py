from discord.ext.menus import ListPageSource
from discord.embeds import Embed


class HelpMenuEmbed(ListPageSource):
    def __init__(self, ctx, data, cmd_description_fnc):
        self.ctx = ctx
        self.cmd_description_fnc = cmd_description_fnc
        super().__init__(data, per_page=7)

    async def write_page(self, menu, fields=[]):
        offset = (menu.current_page*self.per_page) + 1
        len_data = len(self.entries)

        embed = Embed(
            title="Need help with commands?",
            description="This is a list of all available commands and their description, usage, and aliases.",
            colour=self.ctx.author.colour
        )
        embed.set_thumbnail(url=self.ctx.guild.icon_url)
        embed.set_footer(
            text=f"{offset:,} - {min(len_data, offset+self.per_page+1):,} of {len_data:,} commands.")

        for name, value in fields:
            embed.add_field(name=name, value=value, inline=False)

        return embed

    async def format_page(self, menu, entries):
        fields = []

        for entry in entries:
            fields.append((self.cmd_description_fnc(entry),
                          entry.help or "No description"))

        return await self.write_page(menu, fields)
