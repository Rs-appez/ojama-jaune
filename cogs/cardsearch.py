import imp
import json
import string
from discord import Member, Embed
from nextcord.ext import commands
from models.cards import Cards
import requests

class CardSearch(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot = bot
        self.url_ygopro ="https://db.ygoprodeck.com/api/v7/"
        self.url_ygorga ="https://db.ygorganization.com/data/"
        

    @commands.command(name="cards")
    async def search_cards(self, ctx, *name):
        """Search a card"""
        if name != '':
            response_en = requests.get(
                self.url_ygopro + "cardinfo.php?fname=" + "%20".join(name)
            )
            response_fr = requests.get(
                self.url_ygopro + "cardinfo.php?fname=" + "%20".join(name) + '&language=fr'
            )
            if response_en.status_code == 200:
                response = response_en
            elif response_fr.status_code == 200:
                response = response_fr
            else:
                await ctx.send('Aucun résultat')
            cards = list(response.json()['data'])
            ## AFFICHAGE
            if len(cards) == 1:
                # Créer un embed
                
                data = Cards(cards)
                await ctx.send(embed=data.embed())
                
            elif len(cards) <= 50:
                message = f"Listes des cartes trouvées ({len(cards)}):\n"
                message += '--------------------------------\n'
                for card in cards:
                    message += f"{card['name']} \n"
                await ctx.send(f'```{message}```')
            else:
                await ctx.send(f"```Affiner la recherche, il y a trop de résultat ({len(cards)})```")
        else:
            await ctx.send("J'ai besoin d'un nom de carte à rechercher !")

    @commands.command(name="random")
    async def randomcards(self, ctx, *name):
        """Get a random cards"""
        response = requests.get(
            self.url_ygopro + "randomcard.php"
        )
        if(response.status_code == 200):
            await ctx.send(response.json()['card_images'][0]['image_url'])
            await ctx.send("```" + response.json()['desc'] + "```")
    
    @commands.command(name="rulling")
    async def rulling(self, ctx, *name):
        """Rulling from a cards"""
        response_en = requests.get(
            self.url_ygorga + "idx/card/name/en"
        )
        if(response_en.status_code == 200):
            nom = " ".join(name)
            result = dict(response_en.json())
            r = dict((k.lower(), v) for k,v in result.items())
            
            id = r[nom.lower()][0]
            response_rulling = requests.get(
                f'{self.url_ygorga}card/{id}'
            )
            resp:json = response_rulling.json()['faqData']['entries']['0']
            
            find = ''
            for i in resp:
                if 'en' in i:
                    find += i['en'] + '\n'
            if find != '':
                await ctx.send(f'```{find}```')
            else:
                await ctx.send("```Pas de rulling```")
            
            
        
    @commands.command(name="archetype")
    async def archetype(self, ctx, *archetype):
        """List of cartes from a certain archetypes"""
        response = requests.get(
            self.url_ygopro + "cardinfo.php?archetype=" + '+'.join(archetype)
        )
        arch = " ".join(archetype)
        cards = "Listes des cartes de l'archétype " + arch.upper() + ": \n ```"
        for card in response.json()['data']:
            cards += card['name'] + '\n'
        cards += '```'
        await ctx.send(cards) 
        
        
def setup(bot):
    bot.add_cog(CardSearch(bot))