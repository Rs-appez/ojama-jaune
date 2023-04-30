from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command

from models.card.cards import Cards
from models.game.hangman import Hangman


class Game(commands.Cog):
    """some games"""
    def __init__(self,bot):
        self.bot = bot
    @slash_command(name="pendu_yugioh",description="Crois en l'âme des cartes!")
    async def hangman(self,interaction : Interaction ):
        card = Cards.get_random_card()
        hangman = Hangman(card.name,interaction,card.img)
        await hangman.start()

def setup(bot):
    bot.add_cog(Game(bot))