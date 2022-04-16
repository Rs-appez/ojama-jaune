
from nextcord.ext import commands
from config import TEAM_ID

from views.start_tournament_view import StartTournamentView


class Tournament(commands.Cog):
    """Manage yugioh tournament"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command("tournament")
    @commands.has_role(int(TEAM_ID))
    async def create_tournament(self, ctx : commands.Context ):
        """Create a tournament"""

        msg_nb_participant = await ctx.send("Participant : 0")
        await ctx.send("Clique ici pour participer au tournoi !", view=StartTournamentView(msg_nb_participant))
    
        
    @commands.command("start")
    @commands.has_role(int(TEAM_ID))
    async def start_tournament(self, ctx : commands.Context ):
        """start the tournament"""
        await ctx.send("tournoi lancer!")
    
        
def setup(bot):
    bot.add_cog(Tournament(bot))