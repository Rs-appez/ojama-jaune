
import nextcord
from nextcord.ext import commands
from config import DUELIST_ID, TEAM_ID
from models.tournament import Tournament
from views.duelist_view import DuelistView

from views.start_tournament_view import StartTournamentView


class TournamentCog(commands.Cog):
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

        duelists = []

        role_id = int(DUELIST_ID)
        role = ctx.guild.get_role(role_id)
        assert isinstance(role,nextcord.Role)   

        members = ctx.guild.members

        for member in members:
            
            if(role in member.roles):
                duelists.append(member.nick or member.name)
        
        string_member= "__**Liste des duelists**__ :\n\n"
        for duelist in duelists:
            string_member += "> "+duelist+"\n"

        # tournament = Tournament(duelists)

        await ctx.send(string_member, view = DuelistView(ctx))

    
        
def setup(bot):
    bot.add_cog(TournamentCog(bot))