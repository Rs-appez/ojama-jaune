from nextcord.ext import commands
from models.card.opDeck import OpDeck 
class OnePeace(commands.Cog):
    """One piece cmd"""
    def __init__(self,bot):
        self.bot = bot

    
    @commands.command("opc")
    async def convert(self,ctx : commands.Context, * ,args=None ):
        if args:
            deck = OpDeck(args)
            await ctx.send(deck.convert())
  
      
        
def setup(bot):
    bot.add_cog(OnePeace(bot))