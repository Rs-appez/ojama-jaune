import string
from discord import Member
from nextcord.ext import commands

import requests

class CardSearch(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot = bot
        self.challonge_url ="https://db.ygoprodeck.com/api/v7/cardinfo.php"

    @commands.command(name="card")
    async def searchcards(self, ctx, *name):
        """Search a card"""
        
        if(name != ''):
            await ctx.send("Recherche de : " + ' '.join(name))
            response_fr = requests.get(
                self.challonge_url + "?name=" + '+'.join(name) + '&language=fr'
            )
            response_en = requests.get(
                self.challonge_url + "?name=" + '+'.join(name)
            )
            if(response_fr.status_code == 200):
                img = response_fr.json()['data'][0]['card_images'][0]['image_url']
                desc = response_fr.json()['data'][0]['desc']
                await ctx.send(img)
                await ctx.send(desc)
                
            elif(response_fr.status_code == 400):
                if(response_en.status_code == 200):
                    img = response_en.json()['data'][0]['card_images'][0]['image_url']
                    desc = response_en.json()['data'][0]['desc']
                    await ctx.send(img)
                    await ctx.send(desc)
                elif(response_en.status_code == 400):
                    await ctx.send("Soyez plus précis dans le nom de la carte !")
        else:
            await ctx.send("J'ai besoin d'un nom de carte à rechercher !")


def setup(bot):
    bot.add_cog(CardSearch(bot))