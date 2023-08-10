from models.card.cards import Cards
from models.game.guess import Guess
from models.game.player import PlayerTimerThreading,Player
from views.game.battle.starterView import StarterView
from views.game.battle.registerView import RegisterView
from views.game.reload_view import ReloadView

import asyncio

class BattleGuess():

    def __init__(self,author, game_channel,game_manager,emojis) -> None:
        self.channel = game_channel 
        self.emojis = emojis
        self.players = []
        self.author = author
        self.cards = []
        self.finished = False
        self.gm = game_manager

    async def setup(self):
        Cards.get_random_cards(self.cards,5)
        msg = await self.channel.send('Player : \npersonne 😭')
        await self.channel.send('Join the party !',view=RegisterView(self.players,self.emojis["aqua"],msg))
        await self.author.send('Demarrer la partie pour tout les joueurs.',view=StarterView(self))

    async def start(self):
        for player in self.players :
            gbm = GuessBattleManager(self, player)
            await gbm.start()

    async def end(self):
        for player in self.players:
            if not player.has_finish():
                return
        if not self.finished :
            self.finished = True
            await self.channel.send("TIME")

            result = "**__Resultats__** :\n\n"
            medals = {0 : "🥇", 1 : "🥈",2 : "🥉" , 3 : "🤿"}
            for index,player in enumerate(sorted(self.players,key= lambda p : p.points , reverse=True)):
                if index < 4 :
                    result += f"{medals[index]} "
                else :
                    result += f"{index+1} "
                result += f": {player.member.mention} ({player.points} points !)\n"
            await self.channel.send(result)
            await self.channel.send(view=ReloadView(self.gm,self,emojis=self.emojis,others=self.author))

class GuessBattleManager():
    
    def __init__(self,battle_guess,player : Player) -> None:
        self.bg = battle_guess
        self.player = player
        self.card_number = 0

        self.timer = None
    
    async def reload(self,game_channel,correct = None ,emojis = None):
        if not self.timer.finished :
            if correct : self.player.add_point()
            self.card_number += 1
            if self.card_number < len(self.bg.cards):
                await self.__launch_guess()

            else : await self.player.dm(f"tu es trop fort ! 😱")
        
        else : 
            await self.bg.end()

    async def start(self, time = 10):
        await self.player.dm("Let's go !")
        loop = asyncio.get_running_loop()
        self.timer = PlayerTimerThreading(time,self.player,self.bg,loop)
        await self.__launch_guess()

    async def __launch_guess(self):
        guess = Guess(self.bg.cards[self.card_number],self.player.dm_chan,self,self.bg.emojis)
        await guess.start()

