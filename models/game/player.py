from nextcord import Member

class Player():

    def __init__(self,member : Member) -> None:
        self.member = member
        self.dm_chan = None
        self.points = 0

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