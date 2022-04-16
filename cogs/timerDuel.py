from nextcord.ext import commands
from models.timer import Timer
 

class TimerDuel(commands.Cog):
    """Manage timer"""
    def __init__(self,bot):
        self.bot = bot
        self.timer = Timer(time=60)

    

    @commands.command(name="timer")
    async def launch_timer(self,ctx):
        """Timer for a duel"""
        if(not self.timer.started):  
         await self.timer.launch_timer(ctx, self.bot)
        else :
            await ctx.send("le timer est déja lancé !")
      

    @commands.command(name="time")
    async def show_time(self,ctx):
        """get remaining time"""

        if(self.timer.started): 
            time= self.timer.get_time()
            mins, secs = divmod(time, 60)
            time = '{:02d}:{:02d}'.format(mins, secs)
            if(not self.timer.freezed):
                await ctx.send("il reste " + time)
            else :
                await ctx.send("il reste " + time  +" (timer en pause)")
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