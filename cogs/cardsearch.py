import requests
from nextcord import Embed
from nextcord.ext import commands
import config
from models.card.cards import Cards
from nextcord.interactions import Interaction
from nextcord import slash_command

from views.card.rulling_view import RullingView


class CardSearch(commands.Cog):
    """Manage cards commands"""
    def __init__(self,bot):
        self.bot = bot
        self.url_ygopro =config.URL_YGOPRO
        self.url_ygorga =config.URL_YGORGA

        
    @slash_command(name='card',description='Recherche de carte') 
    async def search_cards(self, interaction : Interaction, name : str):
        """Search a card"""
        await interaction.response.defer(with_message=True)
        value : str = name
        card = Cards.search(value)
        ## AFFICHAGE
        if isinstance(card, Cards):
            await interaction.followup.send(embed = card.embed(), view=RullingView(card))
            if 'Ojama' in card.name:
                await interaction.channel.send(content='https://tenor.com/view/yu-gi-oh-gx-ojama-anime-monster-gif-17847003')
        elif isinstance(card, str):
            await interaction.followup.send(content=card)
        else:
            for c in card:
                await interaction.followup.send(embed = c.embed())

    @commands.command(name="archetype")
    async def archetype(self, ctx, *archetype):
        """List of cartes from a certain archetypes"""
        response = requests.get(
            self.url_ygopro + "cardinfo.php?archetype=" + '+'.join(archetype)
        )
        arch = " ".join(archetype)
        cards : str = "Listes des cartes de l'archétype " + arch.upper() + ": \n ```"
        for card in response.json()['data']:
            cards += card['name'] + '\n'
        cards += '```'
        await ctx.send(cards)
        
    @commands.command(name="top")
    async def topDL(self, ctx):
        """List of top deck list"""
        await ctx.send("ALL => " + config.URL_TOP_DL)
        #await ctx.send("YCS => " + config.URL_TOP_YCS)
        #await ctx.send("REGIO => " + config.URL_TOP_REGIO)


    @commands.command(name="random")
    async def randomcards(self, ctx):
        """Get a random cards"""
        card = Cards.get_random_card()
        await ctx.send(embed = card.embed())
            
def setup(bot):
    bot.add_cog(CardSearch(bot))
