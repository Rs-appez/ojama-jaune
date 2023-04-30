from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command

from models.card.cards import Cards
from models.game.hangman import Hangman
from views.hangman.letter_view import Letter_view


class Game(commands.Cog):
    """some games"""
    def __init__(self,bot):
        self.bot = bot
    @slash_command(name="pendu_yugioh",description="Crois en l'âme des cartes!")
    async def hangman(self,interaction : Interaction ):
        # card = Cards.get_random_card()
        hangman = Hangman("test")
        hangman.game_msg = await interaction.send(f"```{hangman.dispaly()}```")
        await interaction.channel.send("Voyelle :",view=Letter_view(hangman,True))
        await interaction.channel.send("Consonne :",view=Letter_view(hangman,False))
def setup(bot):
    bot.add_cog(Game(bot))