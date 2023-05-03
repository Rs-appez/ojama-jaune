from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command

from models.game.gameManager import GameManager


class Game(commands.Cog):
    """some games"""

    def __init__(self,bot):
        self.bot = bot


    @slash_command(name="pendu_yugioh",description="Crois en l'âme des cartes!")
    async def hangman(self,interaction : Interaction ):
        gm = GameManager()
        await gm.hangman_yugioh(interaction)

    @slash_command(name="guess_the_card",description="Crois en l'âme des cartes!")
    async def guess(self,interaction : Interaction ):
        gm = GameManager()
        await gm.guess_the_card(interaction,self.bot.game_emojis)
        

def setup(bot):
    bot.add_cog(Game(bot))