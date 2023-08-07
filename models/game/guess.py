import random
from models.card.cards import Cards
from views.game.guess.typeView import TypeView


class Guess():


    def __init__(self,card : Cards,game_thread,gm,game_emojis):
        self.card = card
        self.gm = gm
        self.game_emojis = game_emojis
        self.game_thread = game_thread
        self.started = False
        self.first_msg = None
        self.msg = None
        self.rdm = random.randrange(0,8)

    async def start(self):
        if not self.started:
            self.started = True
            if self.rdm > 6:
                self.msg = await self.game_thread.send(self.card.img_cropped,view=TypeView(self))
            else : 
                type = self.card.type.lower()
                if "spell" in type: 
                    self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"spell"))
                elif "trap" in type:
                     self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"trap"))
                else :
                    if self.rdm < 1 :
                        self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"attribute"))
                    elif  self.rdm < 2:
                        self.first_msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"race1"))
                        self.second_msg = await  self.game_thread.send(view=TypeView(self,cat="race2",first_view=self.first_view))
                    elif self.rdm < 3 :
                        self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"type_monster_card"))
                    elif self.rdm < 4 and not ("link" in type) :
                        self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"def"))
                    elif self.rdm < 5 :
                        if "link" in type:
                            self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"link"))
                        elif "xyz" in type:
                            self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"rank"))
                        else :
                            self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"level"))
                    else :

                        self.msg = await  self.game_thread.send(self.card.img_cropped,view=TypeView(self,"atk"))
                   
    def check_type(self,type,cat):
        if cat :
            if cat == "attribute":
                return type in self.card.attribute.lower()
            elif "race" in cat:
                return type == self.card.race.lower()
            elif cat == "type_monster_card":
                return type in self.card.type.lower()
            elif cat in ["level","rank","link"]:
                return self.card.level == type
            elif cat == "atk":
                return self.card.atk == int(type)
            elif cat == "def":
                return self.card.defe == int(type)
            return type in self.card.race.lower()
        return type in self.card.type.lower()
    
    async def finish(self):
         await self.game_thread.send(self.card.img)
         await self.gm.reload(self.game_thread,self.game_emojis)


    def generate_stat(self,cat):

        if cat == "atk":
            stat = self.card.atk
        else :
            stat = self.card.defe

        stat_tab = []
        pos = random.randrange(1,6)
        diff = random.randrange(1,10) * 100
        for i in range(pos):
            n_stat = stat - (i * diff)
            if n_stat >= 0 :
                stat_tab.append(n_stat)
        
        stat_tab.sort()

        while stat_tab.__len__() < 5:
            next_stat = stat_tab[-1] + diff
            stat_tab.append(next_stat)

        return stat_tab