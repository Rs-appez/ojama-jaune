from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command,ChannelType

from models.game.gameManager import GameManager
from models.game.scheduler import Scheduler

import config

class Game(commands.Cog):
    """some games"""

    def __init__(self,bot):
        self.bot = bot  
        self.scheduler = Scheduler(self.bot)


    @slash_command(name="pendu_yugioh",description="Crois en l'âme des cartes!")
    async def hangman(self,interaction : Interaction ):
        await self.__start_game(interaction,"pendu_yugioh")

    @slash_command(name="guess_the_card",description="Crois en l'âme des cartes!")
    async def guess(self,interaction : Interaction ):
       await self.__start_game(interaction,"guess_the_card")
        
    @slash_command(name="guess_battle",description="Crois en l'âme des cartes! (plus fort que tes adversaires)",dm_permission=False)
    async def guess_battle(self,interaction : Interaction ):
       await self.__start_game(interaction,"guess_battle")
        

    async def __start_game(self,interaction,game):
        if interaction.channel.type in [ChannelType.news_thread,ChannelType.public_thread,ChannelType.private_thread] :
            await interaction.response.send_message(f"Tu ne peux pas lancer un jeu dans un thread",ephemeral=True)
            return
        gm = GameManager()

        game_channel = await self.__create_game_channel(interaction,game)
        await interaction.response.send_message(f"GAME ! {self.bot.oj_emoji}")

        if game == "guess_the_card":
            await gm.guess_the_card(game_channel,self.bot.game_emojis)
        elif game == "pendu_yugioh" :
            await gm.hangman_yugioh(game_channel)
        elif game == "guess_battle" :
            await gm.guess_battle(interaction.user,game_channel,self.bot.game_emojis)

        

    async def __create_game_channel(self,interaction : Interaction,name_channel):

        if interaction.channel.type == ChannelType.private :
            game_channel = interaction.channel
        else :
            guild = self.bot.get_guild(int(config.GUILD_ID))
            if guild:
                chan = guild.get_channel(int(config.OJAMA_CHANNEL))
            else :
                chan = interaction.channel
            game_channel = await chan.create_thread(name=name_channel,reason = f"{name_channel} started",auto_archive_duration=60,type=ChannelType.public_thread)
        return game_channel

def setup(bot):
    bot.add_cog(Game(bot))