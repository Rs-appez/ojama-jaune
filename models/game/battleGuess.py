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
        Cards.get_random_cards(self.cards,30)
        msg = await self.channel.send('Player : \npersonne 😭')
        emoji = None
        if "millennium" in self.emojis : emoji = self.emojis["millennium"]
        await self.channel.send('Join the party !',view=RegisterView(self.players,emoji,msg))
        await self.author.send('Demarrer la partie pour tout les joueurs.',view=StarterView(self))

    async def start(self):
        for player in self.players :
            gbm = GuessBattleManager(self, player)
            await gbm.start()

    async def end(self):
        if not self.finished:
            self.finished = True
            result = "**__Résultats__** :\n\n"
            medals = {0: "🥇", 1: "🥈", 2: "🥉", 3: "🤿"}

            sorted_players = sorted(self.players, key=lambda p: p.points, reverse=True)
            current_rank = 0
            for index, player in enumerate(sorted_players):
                if index == 0 or player.points != sorted_players[index - 1].points:
                    current_rank = index

                if current_rank < 4:
                    result += f"{medals[current_rank]} "
                else:
                    result += f"{current_rank + 1} "

                result += f": {player.member.mention} ({player.points} points !)\n"

            await self.channel.send(result)
            self.reload_msg = await self.channel.send(view=ReloadView(self.gm, self, emojis=self.emojis, others=self.author))

class GuessBattleManager():
    
    def __init__(self,battle_guess,player : Player) -> None:
        self.bg = battle_guess
        self.player = player
        self.card_number = 0

        self.timer = None
    
    async def reload(self,game_channel,correct = None ,emojis = None):
        if not self.timer.finished :
            self.player.answered += 1
            if correct : self.player.add_point()
            self.card_number += 1
            if self.card_number < len(self.bg.cards):
                await self.__launch_guess()

            else : await self.player.dm(f"tu es trop rapide ! 😱")
        
        else : 
            await self.bg.end()

    async def start(self, time = 60):
        await self.player.dm("Let's go !")
        loop = asyncio.get_running_loop()
        self.timer = PlayerTimerThreading(time,self.player,self.bg,loop)
        await self.__launch_guess()

    async def __launch_guess(self):
        guess = Guess(self.bg.cards[self.card_number]['card'],self.player.dm_chan,self,self.bg.emojis,rdm=self.bg.cards[self.card_number]["rdm"])
        await guess.start()

