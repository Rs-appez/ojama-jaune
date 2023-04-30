from models.card.cards import Cards
from models.game.hangman import Hangman
class GameManager():

    def __init__(self) -> None:
        self.last = None

    async def reload(self,interaction):

        if self.last == "hangman_yugioh":
            await self.hangman_yugioh(interaction)
        
        
    async def hangman_yugioh(self,interaction):
        self.last = "hangman_yugioh"
        card = Cards.get_random_card()
        hangman = Hangman(card.name,interaction,self,card.img)
        await hangman.start()
