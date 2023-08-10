from models.card.cards import Cards

from models.game.guess import Guess

from views.game.battle.starterView import StarterView
from views.game.battle.registerView import RegisterView

class BattleGuess():

    def __init__(self,author, game_channel,emojis) -> None:
        self.channel = game_channel 
        self.emojis = emojis
        self.players = []
        self.author = author
        self.cards = []
    async def setup(self):
        Cards.get_random_cards(self.cards,5)
        msg = await self.channel.send('Player : \npersonne 😭')
        await self.channel.send('Join the party !',view=RegisterView(self.players,self.emojis["aqua"],msg))
        await self.author.send('Demarrer la partie pour tout les joueurs.',view=StarterView(self))

    async def start(self):
        for player in self.players :
            gbm = GuessBattleManager(self, player)
            await gbm.start()

class GuessBattleManager():
    
    def __init__(self,battle_guess,player) -> None:
        self.cards = battle_guess.cards
        self.emojis = battle_guess.emojis
        self.player = player
        self.card_number = 0
    
    async def reload(self,game_channel,correct = None ,emojis = None):
        if correct : self.player.add_point()
        self.card_number += 1
        if self.card_number < len(self.cards):
            await self.__launch_guess()

        else : await self.player.dm(f"tu es trop fort ! 😱")

    async def start(self):
        await self.player.dm("Let's go !")
        await self.__launch_guess()

    async def __launch_guess(self):
        guess = Guess(self.cards[self.card_number],self.player.dm_chan,self,self.emojis)
        await guess.start()