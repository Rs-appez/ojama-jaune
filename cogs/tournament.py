from nextcord.ext import commands

from views.start_tournament_view import StartTournamentView


class Tournament(commands.Cog):
    """Manage yugioh tournament"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command("tournament")
    async def create_tournament(self, ctx : commands.Context ):
        await ctx.send("Clique ici pour participer au tournoi !", view=StartTournamentView())
    
        
def setup(bot):
    bot.add_cog(Tournament(bot))