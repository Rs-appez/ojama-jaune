import json
import string

import requests
from discord import Embed, Member
from nextcord.ext import commands
from models.cards import Cards, CardsRulling


class CardSearch(commands.Cog):
    """Manage cardmarket commands"""
    def __init__(self,bot):
        self.bot = bot
        self.url_ygopro ="https://db.ygoprodeck.com/api/v7/"
        self.url_ygorga ="https://db.ygorganization.com/data/"
        
    @commands.command(name="card")
    async def search_cards(self, ctx, *name):
        """Search a card"""
        if name != '':
            value : str = "%20".join(name)
            card = Cards.search(self, value)
            ## AFFICHAGE
            if isinstance(card, Cards):
                await ctx.send(embed = card.embed())
            else:
                await ctx.send(card)
        else:
            await ctx.send("J'ai besoin d'un nom de carte à rechercher !")


    @commands.command(name="random")
    async def randomcards(self, ctx):
        """Get a random cards"""
        response = requests.get(
            self.url_ygopro + "randomcard.php"
        )
        if response.status_code == 200:
            card = Cards(response.json())
            await ctx.send(embed = card.embed())

    @commands.command(name="rulling")
    async def rulling(self, ctx, *name):
        """Rulling from a cards"""
        response_en = requests.get(
            self.url_ygorga + "idx/card/name/en"
        )
        if response_en.status_code == 200:
            value = " ".join(name)
            card = Cards.search(self, value)
            result = dict(response_en.json())
            r = dict((k.lower(), v) for k,v in result.items())
            
            id = r[card.name.lower()][0]
            response_rulling = requests.get(
                f'{self.url_ygorga}card/{id}'
            )
            try:
                resp = response_rulling.json()['qaIndex']
                card.id_rulling = response_rulling.json()['cardData']['en']['id']
                rullings = list()
                
                if len(resp) > 10:
                    await ctx.send(f"Trop de résultat : {len(resp)}")
                    await ctx.send(f"https://db.ygorganization.com/card#{card.id_rulling}")
                else:
                    for value in resp:
                        response_r = requests.get(
                            f'{self.url_ygorga}qa/{value}'
                        )
                        data = response_r.json()
                        cards = data['cards']
                        id = data['qaData']['en']['id']
                        question = data['qaData']['en']['question']
                        answer = data['qaData']['en']['answer']
                        
                        rulling = CardsRulling(id, cards, question, answer)
                        embed = Embed(title = card.name, url=rulling.url, color=0xff0000)
                        embed.add_field(name="Question", value=rulling.question, inline=False)
                        embed.add_field(name="Answer", value=rulling.answer)
                        rullings.append(embed)
                    await ctx.send(embeds=rullings)
            except KeyError:
                await ctx.send("Erreur")

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
        
        
def setup(bot):
    bot.add_cog(CardSearch(bot))
