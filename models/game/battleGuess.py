from models.card.cards import Cards
from views.game.battle.registerView import RegisterView

from views.game.battle.starterView import StarterView

class BattleGuess():

    def __init__(self,author, game_channel,emojis) -> None:
        self.channel = game_channel 
        self.emojis = emojis
        self.players = []
        self.author = author
        self.cards = []

    async def setup(self):
        Cards.get_random_cards(self.cards,20)
        msg = await self.channel.send('Player : \npersonne 😭')
        await self.channel.send('Join the party !',view=RegisterView(self.players,self.emojis["aqua"],msg))
        await self.author.send('Demarrer la partie pour tout les joueurs.',view=StarterView(self))

    async def start(self):
        print(self.cards)


class GuessBattleManager():
    
    def __init__(self,battle_guess,player) -> None:
        self.cards = battle_guess.cards
        self.emojis = battle_guess.emojis
        self.player = player