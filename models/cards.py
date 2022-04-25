
from discord import Embed
import requests
import json

class Cards():
    def __init__(self, data):
        self.id = data[0]['id']
        self.name = data[0]['name']
        self.type = data[0]['type']
        self.desc = data[0]['desc']
        self.race = data[0]['race']
        self.img = data[0]['card_images'][0]['image_url']
        self.cm = data[0]['card_prices'][0]['cardmarket_price']
        try:
            self.atk = data[0]['atk']
            self.defe = data[0]['def']
            self.level = data[0]['level']
            self.attribute = data[0]['attribute']
        except:
            pass

    def search(self, *name):
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

    def rulling(self, data : json):
        pass

    def embed(self):
        embed=Embed(title=self.name, color=0xff0000)
        embed.set_thumbnail(url=self.img)
        embed.set_author(name=self.id)
        if 'Monster' in self.type:
            embed.add_field(name=self.race, value=f'Level {self.level} / {self.attribute}', inline=True)
            embed.add_field(name="Atk / Def", value=f'{self.atk} / {self.defe}', inline=True)
            embed.add_field(name=self.type, value=self.desc, inline=False)
        elif 'Spell' in self.type or 'Trap' in self.type:
            embed.add_field(name=f'{self.type} {self.race}', value=self.desc, inline=False)
        embed.set_footer(text=f'Prix cardmarket : {self.cm} €')
        return embed