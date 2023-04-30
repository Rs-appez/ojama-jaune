from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command

from models.cards import Cards
from models.hangman import Hangman


class Game(commands.Cog):
    """some games"""
    def __init__(self,bot):
        self.bot = bot

    @slash_command(name="pendu_yugioh",description="Crois en l'âme des cartes!")
    async def hangman(self,interaction : Interaction ):
        # card = Cards.get_random_card()
        hangman = Hangman()
        game_msg = await interaction.send(f"```{hangman.dispaly()}```")
        for i in range(10):
            hangman.add_error()
            await game_msg.edit(f"```{hangman.dispaly()}```")
      
        
def setup(bot):
    bot.add_cog(Game(bot))