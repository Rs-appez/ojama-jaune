from nextcord.ext import commands
from models.timer import Timer
 

class TimerDuel(commands.Cog):
    """Manage timer"""
    def __init__(self,bot):
        self.bot = bot
        self.timer = Timer()

    

    @commands.command(name="timer")
    async def launch_timer(self,ctx, temps:int = 40):
        """Timer for a duel"""
        if(not self.timer.started):  
         await self.timer.launch_timer(ctx, temps*60)
        else :
            await ctx.send("le timer est déja lancé !")
      

    @commands.command(name="time")
    async def show_time(self,ctx):
        """get remaining time"""

        if(self.timer.started): 
            await self.timer.get_time()
            
        else :
            await ctx.send("le timer n'est pas lancé !")

    @commands.command()
    async def stop(self,ctx):
        """stop timer"""

        self.timer.stop()
        await ctx.send("le timer a été arreté")

        
    # @commands.command()
    # async def freeze(self,ctx):
    #     """freeze timer"""

    #     self.timer.freeze()
    #     if(self.timer.freezed):
    #         await ctx.send("le timer a été mit en pause")
    #     else :
    #          await ctx.send("le timer a redémarré")

        
def setup(bot):
    bot.add_cog(TimerDuel(bot))