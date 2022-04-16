from nextcord.ext import commands
from models.timer import Timer
 

class Tournament(commands.Cog):
    """Manage yugioh tournament"""
    def __init__(self,bot):
        self.bot = bot
        self.timer = Timer( 20)

    

    @commands.command(name="timer")
    async def launch_timer(self,ctx):
        """Timer for a duel"""
        if(not self.timer.started):  
         await self.timer.launch_timer(ctx, self.bot)
        else :
            await ctx.send("le timer est déja lancé !")
      

    @commands.command()
    async def time(self,ctx):
        """get timer for a duel"""

        if(self.timer.started): 
            time= self.timer.get_time()
            await ctx.send("il reste " + time)
        else :
            await ctx.send("le timer n'est pas lancé !")

        
def setup(bot):
    bot.add_cog(Tournament(bot))