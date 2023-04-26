from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command

class Game(commands.Cog):
    """some games"""
    def __init__(self,bot):
        self.bot = bot

    @slash_command(name="pendu yugioh",description="Crois en l'âme des cartes!")
    async def convert(self,interaction : Interaction ):
        pass
      
        
def setup(bot):
    bot.add_cog(Game(bot))