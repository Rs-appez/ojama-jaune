import asyncio

class Timer():
    def __init__(self,time = 2400):
        self._time = time
        self._time_remaining = time
        self.time = "Not started"

    def get_time(self):
        return self.time

    async def start(self):

        while(self._time_remaining):
            mins, secs = divmod(self._time_remaining, 60)
            self.time = '{:02d}:{:02d}'.format(mins, secs)
            print(self.time, end="\r")
            await asyncio.sleep(1)
            self._time_remaining -= 1


        self._time_remaining = self._time
        self.time = "Not started"

    async def launch_timer(self, ctx, bot):
        await ctx.send(5)
        for i in range(5):           
            async for message in ctx.message.channel.history(limit = 1):
                if(message.author == bot.user):
                    await asyncio.sleep(1)
                    if(i != 4):
                        await message.edit(content=4-i)
                    else:
                        await message.edit(content="TIME TO DUEL")
        await self.start()

        await ctx.send("TIME !!!!!!!!!!!!!!")