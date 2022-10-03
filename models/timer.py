import asyncio
import time as T
from nextcord import  Role

from config import DUELIST_ID

class Timer():
    def __init__(self):
        self.started = False
        self.freezed = False

    def get_time_remianing(self) :
        return (self.time - (T.time() - self.started_time)).__floor__()

    async def get_time(self):
        time_remaining = self.get_time_remianing()
        mins, secs = divmod(time_remaining, 60)
        time = '{:02d}:{:02d} min'.format(mins, secs)
        if(not self.freezed):
            await self.ctx.send("il reste " + time)
        else :
            await self.ctx.send("il reste " + time  +" (timer en pause)")

    def stop(self):
        self.started = False

    def freeze(self):
        self.freezed = not self.freezed

    async def start(self):
        self.started_time = T.time()
        while self.started :
            await asyncio.sleep(1)
            time_remaining = self.get_time_remianing()
            if   time_remaining <= 0 :
                self.started = False
            elif time_remaining%600 == 0 : 
                await self.get_time()

    async def launch_timer(self, ctx, time):

        self.ctx = ctx
                
        role_id = int(DUELIST_ID)
        duelist_role : Role = ctx.guild.get_role(role_id)

        self.time = time
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
