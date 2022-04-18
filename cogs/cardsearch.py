import json
import string
from discord import Member
from nextcord.ext import commands

import requests

class CardSearch(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot = bot
        self.url_ygopro ="https://db.ygoprodeck.com/api/v7/"
        self.url_ygorga ="https://db.ygorganization.com/data/"
        

    @commands.command(name="card")
    async def searchcards(self, ctx, *name):
        """Search a card"""
        
        if(name != ''):
            await ctx.send("Recherche de : " + ' '.join(name))
            response_fr = requests.get(
                self.url_ygopro + "cardinfo.php?name=" + '+'.join(name) + '&language=fr'
            )
            response_en = requests.get(
                self.url_ygopro + "cardinfo.php?name=" + '+'.join(name)
            )
            if(response_fr.status_code == 200):
                img = response_fr.json()['data'][0]['card_images'][0]['image_url']
                desc = response_fr.json()['data'][0]['desc']
                await ctx.send(img)
                await ctx.send("```" + desc + "```")
                
            elif(response_fr.status_code == 400):
                if(response_en.status_code == 200):
                    img = response_en.json()['data'][0]['card_images'][0]['image_url']
                    desc = response_en.json()['desc'][0]['desc']
                    await ctx.send(img)
                    await ctx.send("```" + desc + "```")
                elif(response_en.status_code == 400):
                    await ctx.send("Soyez plus précis dans le nom de la carte !")
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
            id = response_en.json()[" ".join(name)][0]       
            response_rulling = requests.get(
                f'{self.url_ygorga}card/{id}'
            )
            resp:json = response_rulling.json()['faqData']['entries']['0']
            for r in resp:
                if 'en' in r:
                    await ctx.send(f"```{r['en']}```")
        
        
def setup(bot):
    bot.add_cog(CardSearch(bot))