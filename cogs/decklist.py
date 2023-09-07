from nextcord.ext import commands
import config

class Decklist(commands.Cog):
    """All for the best decklist"""
    def __init__(self,bot):
        self.bot = bot
        
    @commands.command(name="top")
    async def topDL(self, ctx):
        """List of top deck list"""
        await ctx.send("ALL => " + config.URL_TOP_DL)
        #await ctx.send("YCS => " + config.URL_TOP_YCS)
        await ctx.send("REGIO => " + config.URL_TOP_REGIO)

def setup(bot):
    bot.add_cog(Decklist(bot))
