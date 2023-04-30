from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command

from models.cards import Cards


class Game(commands.Cog):
    """some games"""
    def __init__(self,bot):
        self.bot = bot

    @slash_command(name="pendu_yugioh",description="Crois en l'âme des cartes!")
    async def hangman(self,interaction : Interaction ):
        card = Cards.get_random_card()
        await interaction.send(card.name)
      
        
def setup(bot):
    bot.add_cog(Game(bot))