import asyncio
import time as T
from nextcord import  Role

from config import DUELIST_ID

class Timer():
    def __init__(self, channel):
        self.started = False
        self.freezed = False
        self.channel = channel
    
    def get_time_remianing(self) :
        return (self.time - (T.time() - self.started_time)).__floor__()
    
    def get_time_str(self):
        time_remaining = self.get_time_remianing()
        mins, secs = divmod(time_remaining, 60)
        return '{:02d}:{:02d} min'.format(mins, secs)

    async def get_time(self, response = None):
        time = self.get_time_str()
        if response :
            if(not self.freezed):
                await response.send_message("il reste " + time)
            else :
                await response.send_message("il reste " + time  +" (timer en pause)")
        else :
            if(not self.freezed):
                await self.channel.send("il reste " + time)
            else :
                await self.channel.send("il reste " + time  +" (timer en pause)")

    def stop(self):
        self.started = False

    def freeze(self):
        self.freezed = not self.freezed

    async def start(self):
        self.started_time = T.time()
        while self.started :
            await asyncio.sleep(1)
            await self.channel.edit(name = f'TIME : {self.get_time_str()}')
            time_remaining = self.get_time_remianing()
            if   time_remaining <= 0 :
                self.started = False
            elif time_remaining%600 == 0 : 
                await self.get_time()

    async def launch_timer(self, interaction, time):

        self.channel = interaction.channel
                
        role_id = int(DUELIST_ID)
        duelist_role : Role = interaction.guild.get_role(role_id)

        self.time = time
        self.started = True
        message = await self.channel.send(5)
        for i in range(4):           
            await asyncio.sleep(1)
            await message.edit(content=4-i)
        
        await message.delete()

        if(duelist_role):
            await self.channel.send(content=f"TIME TO DUEL {duelist_role.mention}")
        else : 
            await self.channel.send(content=f"TIME TO DUEL")

        await self.start()

        if(duelist_role):
            await self.channel.send(f"TIME !!!!!!!!!!!!!! {duelist_role.mention}")
        else : 
            await self.channel.send(f"TIME !!!!!!!!!!!!!!")