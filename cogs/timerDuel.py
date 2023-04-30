from nextcord.ext import commands
from nextcord.interactions import Interaction
from nextcord import slash_command
from models.tournament.timer import Timer
 

class TimerDuel(commands.Cog):
    """Manage timer"""
    def __init__(self,bot):
        self.bot = bot
        self.timer = Timer()

    @slash_command(name='start_timer',description='Start timer')
    async def launch_timer(self,interaction : Interaction, minutes:int = 40):
        """Timer for a duel"""
        if(not self.timer.started):  
            await interaction.response.send_message(content="le timer est lancé !",ephemeral=True)
            await self.timer.launch_timer(interaction, minutes*60)
        else :
            await interaction.response.send_message("le timer est déja lancé !",ephemeral=True)
      

    @slash_command(name='time',description='Get remaining time of the timer')
    async def show_time(self,interaction):
        """get remaining time"""

        if(self.timer.started): 
            await self.timer.get_time(interaction.response)
            
        else :
            await interaction.response.send_message("le timer n'est pas lancé !")

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