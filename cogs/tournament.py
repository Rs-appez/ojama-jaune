from nextcord.ext import commands


class Tournament(commands.Cog):
    """Manage yugioh tournament"""
    def __init__(self,bot):
        self.bot = bot

    
        
def setup(bot):
    bot.add_cog(Tournament(bot))