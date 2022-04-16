import asyncio

class Timer():
    def __init__(self,time = 2400):
        self._time = time
        self._time_remaining = time
        self.started = False
        self.freezed = False

    def get_time(self):
        return self._time_remaining

    def stop(self):
        self._time_remaining = 0

    def freeze(self):
        self.freezed = not self.freezed

    async def start(self):
        
        while(self._time_remaining > 0):
            await asyncio.sleep(1)
            self._time_remaining -= 1
        self._time_remaining = self._time

    async def launch_timer(self, ctx, time):
        self._time_remaining = time
        self.started = True
        message = await ctx.send(5)
        for i in range(5):           
            await asyncio.sleep(1)
            if(i != 4):
                await message.edit(content=4-i)
            else:
                await message.edit(content="TIME TO DUEL")
        await self.start()

        await ctx.send("TIME !!!!!!!!!!!!!! @everyone")
        self.started = False
