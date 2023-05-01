import random
from models.card.cards import Cards
from views.game.guess.typeView import TypeView


class Guess():

    __game_msg = None

    def __init__(self,card : Cards,interaction,gm,game_emojis):
        self.card = card
        self.interaction = interaction
        self.gm = gm
        self.game_emojis = game_emojis
        self.started = False
        self.rdm = random.randrange(0,12)

    async def start(self):
        if not self.started:
            self.started = True
            self.__game_msg = await self.interaction.send(self.card.img_cropped,view=TypeView(self))

    def check_type(self,type):
        
        return type in self.card.type.lower()
    
    async def finish(self):
         await self.interaction.channel.send(self.card.img)
         await self.gm.reload(self.interaction,self.game_emojis)
