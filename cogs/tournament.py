
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
        self.test = True

    @commands.command("tournament")
    @commands.has_role(int(TEAM_ID))
    async def create_tournament(self, ctx : commands.Context ):
        """Create a tournament"""

        msg_nb_participant = await ctx.send("Participant : 0")
        await ctx.send("Clique ici pour participer au tournoi !", view=StartTournamentView(msg_nb_participant))
    
        
    @commands.command("validate")
    @commands.has_role(int(TEAM_ID))
    async def validate_tournament(self, ctx : commands.Context ):
        """start the tournament"""

        duelists = []

        role_id = int(DUELIST_ID)
        role = ctx.guild.get_role(role_id)
        assert isinstance(role,nextcord.Role)   

        members = ctx.guild.members

        for member in members:
            
            if(role in member.roles):
                if(member.nick):
                    name = member.nick.lower()
                else :
                    name = member.name.lower()

                duelists.append(name)

        
        #for test api test API
        if(self.test):
            duelists = ["joueur A","joueur B","joueur C", "reponse D","appez","ojama jaune","ojama noir","ojama vert","ojama rouge",'ojama bleu','ojama rose',".ojama roi",'ojama knight',"ojama emperor"]

        duelists.sort()

        string_member= "__**Liste des duelists**__ :\n\n"
        for duelist in duelists:
            string_member += "> "+duelist+"\n"


        self.tournament = Tournament(ctx,duelists)

        await ctx.send(string_member, view = DuelistView(ctx, self.tournament))

    @commands.command()
    @commands.is_owner()
    async def delete(self, ctx):
        await Tournament.dell_all_tournament(ctx)


    @commands.command("p")
    @commands.is_owner()
    async def get_participant(self, ctx):
        await self.tournament.get_participant()

        
    @commands.command("matches")
    async def matches_tournament(self, ctx):
        await self.tournament.matches()

        
def setup(bot):
    bot.add_cog(TournamentCog(bot))