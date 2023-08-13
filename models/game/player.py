from nextcord import Member
import threading
import time
import asyncio

class Player():

    def __init__(self,member : Member) -> None:
        self.member = member
        self.dm_chan = None
        self.points = 0
        self.answered = 0
        self.finished = False

    def __str__(self) -> str:
        if self.member.nick :
            return self.member.nick
        else :
            return self.member.name
        
    async def dm(self,msg,view = None):
        if not self.dm_chan:
            await self.setup_dm_channel()
        await self.dm_chan.send(msg,view=view)

    async def get_dm_url(self) :
        if not self.dm_chan:
            await self.setup_dm_channel()      
        return self.dm_chan.jump_url

    def add_point(self,points = 1):
        self.points += points

    def get_accuracy(self):
        return (self.points/self.answered)*100
    
    def has_finish(self) -> bool:
        return self.finished

    async def setup_dm_channel(self):
        self.dm_chan = await self.member.create_dm()

class PlayerTimerThreading(object):

    def __init__(self, seconds,player : Player, battle_guess,loop ):
        self.player = player
        self.seconds = seconds
        self.start_time = time.time()
        self.finished = False
        self.loop = loop
        self.bg = battle_guess

        thread = threading.Thread(target=self.run, args=[self.loop])
        thread.daemon = True
        thread.start()

    def run(self,loop):
        while not self.finished :
            if time.time() - self.start_time >= self.seconds:
                self.finished = True
        self.player.finished = True
        asyncio.run_coroutine_threadsafe(self.send_time(), loop)

    async def send_time(self):
        await self.player.dm("📯 TIME 📯")
        await self.player.dm(f"Retour au thread :\n➡{self.bg.channel.jump_url}⬅")
        await self.bg.end()