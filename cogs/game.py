from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command,ChannelType

from models.game.gameManager import GameManager


class Game(commands.Cog):
    """some games"""

    def __init__(self,bot):
        self.bot = bot


    @slash_command(name="pendu_yugioh",description="Crois en l'âme des cartes!")
    async def hangman(self,interaction : Interaction ):
        gm = GameManager()
        game_channel = await self.create_game_channel(interaction,"pendu")
        await gm.hangman_yugioh(game_channel)

    @slash_command(name="guess_the_card",description="Crois en l'âme des cartes!")
    async def guess(self,interaction : Interaction ):
        gm = GameManager()
        game_channel = await self.create_game_channel(interaction,"guess the card")
        await gm.guess_the_card(game_channel,self.bot.game_emojis)
        
    async def create_game_channel(self,interaction : Interaction,name_channel):

        if interaction.channel.type == ChannelType.private :
            game_channel = interaction.channel
        else :
            game_channel = await interaction.channel.create_thread(name=name_channel,reason = f"{name_channel} started",auto_archive_duration=60)
            await game_channel.add_user(interaction.user)
        return game_channel

def setup(bot):
    bot.add_cog(Game(bot))