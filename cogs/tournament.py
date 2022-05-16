
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
        self.tournament = None

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
        duelists_str = []

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

                duelists_str.append(name)
                duelists.append(member)

      
        duelists_str.sort()

        string_member= "__**Liste des duelists**__ :\n\n"
        for duelist in duelists_str:
            string_member += "> "+duelist+"\n"


        self.tournament = Tournament(ctx,duelists)

        await ctx.send(string_member, view = DuelistView(ctx, self.tournament))

    @commands.command()
    @commands.is_owner()
    async def delete(self, ctx):
        await Tournament.dell_all_tournament(ctx)

                
    @commands.command("win")
    @commands.has_role(int(DUELIST_ID))
    async def set_win(self, ctx, *score : int):
        if(self.tournament):
            if(score and score[0] > score[1] and 
                score[0] > 0 and score[0] <=2 and
                score[1] >= 0 and score[1] <2):
                await self.tournament.set_win(ctx.author,score[0],score[1])
            else :
                await ctx.send("Utiliser la commande comme ceci :\n !win 2 0\n ou\n !win 2 1")
        else :
            await ctx.send("Pas de tournoi en cours")
                
    @commands.command("draw")
    @commands.has_role(int(DUELIST_ID))
    async def set_draw(self, ctx, *score : int):
        if(self.tournament):
            if(score and (score[0] == 1 or score[0] == 0)):
                await self.tournament.set_draw(ctx.author, score[0])
            else:
                await ctx.send("Utiliser la commande comme ceci :\n !draw 1\n ou\n !draw 0")
        else :
            await ctx.send("Pas de tournoi en cours")
    
    @commands.command("finish")
    async def finish_tournament(self,ctx):
        await self.tournament.finish_tournament()
    
    @commands.command("delete_vocal")
    @commands.is_owner()
    async def delete_vocal_tournament(self, ctx):
        await self.tournament.dell_vocal(self)


    @commands.command()
    @commands.is_owner()
    async def clean(self, ctx):

        if(self.tournament):
            await self.tournament.dell_vocal(self)

        role_id = int(DUELIST_ID)
        role = ctx.guild.get_role(role_id)
        assert isinstance(role,nextcord.Role)   

        members = ctx.guild.members

        for member in members:
            
            if(role in member.roles):
               await member.remove_roles(role)

    
    
    @commands.command("launch_vocal_round")
    @commands.has_role(int(TEAM_ID))
    async def launch_vocal_round(self,ctx):
        await Tournament.launch_vocal_round(ctx)
    
def setup(bot):
    bot.add_cog(TournamentCog(bot))