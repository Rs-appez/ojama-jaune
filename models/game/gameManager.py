from models.card.cards import Cards
from models.game.guess import Guess
from models.game.hangman import Hangman
class GameManager():

    def __init__(self) -> None:
        self.last = None

    async def reload(self,interaction,other = None):

        if self.last == "hangman_yugioh":
            await self.hangman_yugioh(interaction)
        elif self.last == "guess_the_card":
            await self.guess_the_card(interaction,other)
        
        
    async def hangman_yugioh(self,interaction):
        self.last = "hangman_yugioh"
        card = Cards.get_random_card()
        hangman = Hangman(card.name,interaction,self,card.img)
        await hangman.start()
        
        
    async def guess_the_card(self,interaction,game_emojis):
        self.last = "guess_the_card"
        card = Cards.get_random_card()
        guess = Guess(card,interaction,self,game_emojis)
        await guess.start()
