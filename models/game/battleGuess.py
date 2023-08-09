from models.card.cards import Cards
from views.game.battle.registerView import RegisterView
import asyncio

from views.game.battle.starterView import StarterView

class BattleGuess():

    def __init__(self,author, game_channel,emojis) -> None:
        self.channel = game_channel 
        self.emojis = emojis
        self.players = []
        self.author = author
        self.cards = []

    async def setup(self):
        msg = await self.channel.send('Player : \npersonne 😭')
        await self.channel.send('Join the party !',view=RegisterView(self.players,self.emojis["aqua"],msg))
        self.get_cards()
        await self.author.send('Demarrer la partie pour tout les joueurs.',view=StarterView(self))
        print(self.cards)

    async def start(self):
        print('ok')

    def get_cards(self):
        
        for i in range(5):
            self.cards.append(Cards.get_random_card())

        