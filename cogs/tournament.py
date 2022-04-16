from nextcord.ext import commands
import asyncio
from models.timer import Timer
 

class Tournament(commands.Cog):
    """Manage yugioh tournament"""
    def __init__(self,bot):
        self.bot = bot
        self.timer = Timer( 20)

    

    @commands.command()
    async def timer(self,ctx):
        """Timer for a duel"""

        await self.timer.launch_timer(ctx, self.bot)
      

    @commands.command()
    async def time(self,ctx):
        """get timer for a duel"""

        time= self.timer.get_time()
        await ctx.send("il reste " + time)


        
def setup(bot):
    bot.add_cog(Tournament(bot))