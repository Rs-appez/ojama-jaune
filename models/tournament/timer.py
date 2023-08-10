import asyncio
import threading
import time as T
from nextcord import  Role

from config import DUELIST_ID

class Timer():
    def __init__(self):
        self.started = False
        self.freezed = False

    def get_time_remianing(self) :
        return (self.time - (T.time() - self.started_time)).__floor__()

    async def get_time(self, response = None):
        time_remaining = self.get_time_remianing()
        mins, secs = divmod(time_remaining, 60)
        time = '{:02d}:{:02d} min'.format(mins, secs)
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

class TimerThreading(object):

    def __init__(self, seconds):
        self.seconds = seconds
        self.start_time = T.time()
        self.finished = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        asyncio.run(self.timer())

    async def timer(self):
        while not self.finished :
            if T.time() - self.start_time >= self.seconds:
                self.finished = True