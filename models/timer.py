import asyncio

from discord import  Role

from config import DUELIST_ID

class Timer():
    def __init__(self,time = 2400):
        self._time = time
        self._time_remaining = time
        self.started = False
        self.freezed = False

    async def get_time(self):
        mins, secs = divmod(self._time_remaining, 60)
        time = '{:02d}:{:02d}'.format(mins, secs)
        if(not self.freezed):
            await self.ctx.send("il reste " + time)
        else :
            await self.ctx.send("il reste " + time  +" (timer en pause)")

    def stop(self):
        self._time_remaining = 0

    def freeze(self):
        self.freezed = not self.freezed

    async def start(self):
        
        while(self._time_remaining > 0):
            await asyncio.sleep(1)
            self._time_remaining -= 1
            if(self._time_remaining%600 == 0): 
                await self.get_time()
        self._time_remaining = self._time

    async def launch_timer(self, ctx, time):

        self.ctx = ctx
                
        role_id = int(DUELIST_ID)
        duelist_role : Role = ctx.guild.get_role(role_id)

        self._time_remaining = time
        self.started = True
        message = await ctx.send(5)
        for i in range(4):           
            await asyncio.sleep(1)
            await message.edit(content=4-i)
        
        await message.delete()

        if(duelist_role):
            await ctx.send(content=f"TIME TO DUEL {duelist_role.mention}")
        else : 
            await ctx.send(content=f"TIME TO DUEL")
        await self.start()

        if(duelist_role):
            await ctx.send(f"TIME !!!!!!!!!!!!!! {duelist_role.mention}")
        else : 
            await ctx.send(f"TIME !!!!!!!!!!!!!!")
        self.started = False
