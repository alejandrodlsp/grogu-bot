class Embed:
    async def send(self):
        self.msg = await self.ctx.send(embed=self.embed)
        return self.msg
        