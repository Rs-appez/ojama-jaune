import random
from models.card.cards import Cards
from views.game.guess.typeView import TypeView


class Guess():


    def __init__(self,card : Cards,interaction,gm,game_emojis):
        self.card = card
        self.interaction = interaction
        self.gm = gm
        self.game_emojis = game_emojis
        self.started = False
        self.rdm = random.randrange(0,8)

    async def start(self):
        if not self.started:
            self.started = True
            if self.rdm > 6 :
                await self.interaction.send(self.card.img_cropped,view=TypeView(self))
            else : 
                type = self.card.type.lower()
                if "spell" in type: 
                    await self.interaction.send(self.card.img_cropped,view=TypeView(self,"spell"))
                elif "trap" in type:
                    await self.interaction.send(self.card.img_cropped,view=TypeView(self,"trap"))
                else :
                    if True :
                        await self.interaction.send(self.card.img_cropped,view=TypeView(self,"attribute"))
                    else :
                        await self.interaction.send(self.card.img_cropped,view=TypeView(self))
    def check_type(self,type,cat):
        if cat :
            if cat == "attribute":
                return type in self.card.attribute.lower()
            return type in self.card.race.lower()
        return type in self.card.type.lower()
    
    async def finish(self):
         await self.interaction.channel.send(self.card.img)
         await self.gm.reload(self.interaction,self.game_emojis)