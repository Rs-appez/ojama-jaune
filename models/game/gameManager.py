from models.card.cards import Cards
from models.game.guess import Guess
from models.game.hangman import Hangman
class GameManager():

    def __init__(self) -> None:
        self.last = None

    async def reload(self,game_channel,other = None):

        if self.last == "hangman_yugioh":
            await self.hangman_yugioh(game_channel)
        elif self.last == "guess_the_card":
            await self.guess_the_card(game_channel,other)
        
        
    async def hangman_yugioh(self,game_channel):
        self.last = "hangman_yugioh"
        card = Cards.get_random_card()
        hangman = Hangman(card.name,game_channel,self,card.img)
        await hangman.start()
        
        
    async def guess_the_card(self,game_channel,game_emojis):
        self.last = "guess_the_card"
        card = Cards.get_random_card()
        guess = Guess(card,game_channel,self,game_emojis)
        await guess.start()
