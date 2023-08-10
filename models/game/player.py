from nextcord import Member
import threading
import time
class Player():

    def __init__(self,member : Member) -> None:
        self.member = member
        self.dm_chan = None
        self.points = 0
        self.finished = False

    def __str__(self) -> str:
        if self.member.nick :
            return self.member.nick
        else :
            return self.member.name
        
    async def dm(self,msg,view = None):
        if not self.dm_chan :
            self.dm_chan = await self.member.create_dm()
        await self.dm_chan.send(msg,view=view)

    def add_point(self,points = 1):
        self.points += points
    
    def has_finish(self) -> bool:
        return self.finished

class PlayerTimerThreading(object):

    def __init__(self, seconds,player : Player):
        self.player = player
        self.seconds = seconds
        self.start_time = time.time()
        self.finished = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while not self.finished :
            if time.time() - self.start_time >= self.seconds:
                self.finished = True
        self.player.finished = True