from typing import List
from nextcord import Embed
import requests
import json

class Cards():
    _url_ygopro = "https://db.ygoprodeck.com/api/v7/"
    _url_ygorga = "https://db.ygorganization.com/data/"
    
    def __init__(self, data : json):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.desc = data['desc']
        self.race = data['race']
        self.img = data['card_images'][0]['image_url']
        self.cm = data['card_prices'][0]['cardmarket_price']
        try:
            self.atk = data['atk']
            self.defe = data['def']
            self.level = data['level']
            self.attribute = data['attribute']
        except:
            pass
        self.id_rulling = None

    def search(self, name : str):
        response_en = requests.get(
            Cards._url_ygopro + "cardinfo.php?fname=" + name
        )
        response_fr = requests.get(
            Cards._url_ygopro + "cardinfo.php?fname=" + name + '&language=fr'
        )
        if response_en.status_code == 200:
            response = response_en
        elif response_fr.status_code == 200:
            response = response_fr
        else:
            return "Carte non trouvée !"
        try:
            data = response.json()['data']
        except KeyError:
            data = response.json()[0]
        if len(data) == 1:
            card = Cards(data[0])
            return card
        elif len(data) <= 3:
            cards = []
            for card in data:
                c = Cards(card)
                cards.append(c)
            return cards
        elif len(data) <= 50:
            message = f"```Listes des cartes trouvées ({len(data)}):\n"
            message += '--------------------------------\n'
            for card in data:
                message += f"{card['name']} \n"
            return message + "```"
        else:
            message = f"Affiner la recherche, il y a {len(data)} résultats"
            return message


    def rulling(self):
        pass

    def embed(self):
        """Return a discord.Embed"""
        embed=Embed(title=self.name, color=0xff0000)
        embed.set_thumbnail(url=self.img)
        embed.set_author(name=self.id)
        if 'Monster' in self.type:
            embed.add_field(name=self.race, value=f'Level {self.level} / {self.attribute}', inline=True)
            embed.add_field(name="Atk / Def", value=f'{self.atk} / {self.defe}', inline=True)
            embed.add_field(name=self.type, value=self.desc, inline=False)
        elif 'Spell' in self.type or 'Trap' in self.type:
            embed.add_field(name=f'{self.type} - {self.race}', value=self.desc, inline=False)
        embed.set_footer(text=f'Prix cardmarket : {self.cm} €')
        return embed

    def __str__(self) -> str:
        message = ''
        message += f"{self.id} {self.name} \n"
        message += f"{self.desc}"
        return message

class CardsRulling():
    _url_ygorga = "https://db.ygorganization.com/data/"
    def __init__(self, id : int, cards : List, question : str, answer : str) -> None:
        names = {}
        for c in cards:
            response = requests.get(
                f'{CardsRulling._url_ygorga}card/{c}'
            )
            if response.status_code == 200:
                name : str = response.json()['cardData']['en']['name']
                names[c] = name
        
        for key, value in names.items():
            question = question.replace(f'<<{key}>>', f"[{value.upper()}]")
            answer = answer.replace(f'<<{key}>>', f"[{value.upper()}]")
        self.question = question
        self.answer = answer
        self.cards = names
        self.id = id
        self.url = "https://db.ygorganization.com/qa#" + str(id)
