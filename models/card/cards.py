from typing import List
from nextcord import Embed
import requests
import json
from nextcord.interactions import Interaction
import threading
import time

from config import URL_YGOPRO, URL_YGORGA
from models.game.guess import Guess

class Cards():
    _url_ygopro = URL_YGOPRO
    _url_ygorga = URL_YGORGA
    
    def __init__(self, data : json):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.desc = data['desc']
        self.race = data['race']
        self.img = data['card_images'][0]['image_url']
        self.img_cropped = self.img.replace("cards","cards_cropped")
        self.cm = data['card_prices'][0]['cardmarket_price']
        
        if self.type != 'Spell Card' and self.type != 'Trap Card':
            self.atk = data['atk']
            self.attribute = data['attribute']
            if self.type == 'Link Monster':
                self.level = data['linkval']
            else:
                self.defe = data['def']
                self.level = data['level']
                
        response_en = requests.get(
            self._url_ygorga + "idx/card/name/en"
        )
        if response_en.status_code == 200:
            result = dict(response_en.json())
            r = dict((k.lower(), v) for k,v in result.items())
            try :
                id = r[self.name.lower()][0]
            except :  
                id = 0
        self.id_rulling = id
    @staticmethod
    def get_random_card():
        response_type = "skill"
        while "skill" in response_type.lower() or "token" in response_type.lower():
            response = requests.get(
                Cards._url_ygopro + "randomcard.php"
            )
            if response.status_code == 200:
                response_type = response.json()['type']
            else : break
        if response.status_code == 200:
            return Cards(response.json())
        
    @staticmethod
    def get_random_cards(cards_list,nb_cards):
        CardThreading(cards_list,nb_cards)


    @staticmethod
    def search(name : str):
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
            
            resp = requests.get(
                Cards._url_ygopro + "idx/card/name/en"
            )
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


    async def rulling(self, interaction : Interaction):
        response_rulling = requests.get(
                f'{self._url_ygorga}card/{self.id_rulling}'
            )
        try:
            resp = response_rulling.json()['qaIndex']
            rullings = list()
            
            if len(resp) > 10:
                await interaction.followup.send(f"Trop de résultat : {len(resp)} \n https://db.ygorganization.com/card#{self.id_rulling}")
            else:
                for value in resp:
                    response_r = requests.get(
                        f'{self._url_ygorga}qa/{value}'
                    )
                    data = response_r.json()
                    cards = data['cards']
                    id = data['qaData']['en']['id']
                    question = data['qaData']['en']['question']
                    answer = data['qaData']['en']['answer']
                    
                    rulling = CardsRulling(id, cards, question, answer)
                    embed = Embed(title = self.name, url=rulling.url, color=0xff0000)
                    embed.add_field(name="Question", value=rulling.question, inline=False)
                    embed.add_field(name="Answer", value=rulling.answer)
                    rullings.append(embed)
                for r in rullings:
                    await interaction.channel.send(embed=r)
                
                await interaction.followup.send(content = str(len(rullings)) + ' rullings trouvés !')
        except KeyError:
            await interaction.channel.send("Erreur")
        

    def embed(self):
        """Return a discord.Embed"""
        embed=Embed(title=self.name, color=0xff0000)
        embed.set_thumbnail(url=self.img)
        embed.set_author(name=self.id)
        if 'Monster' in self.type:
            if 'Link' in self.type:
                embed.add_field(name=self.race, value=f'Link - {self.level} / {self.attribute}', inline=True)
                embed.add_field(name="Atk", value=f'{self.atk}', inline=True)
                embed.add_field(name=self.type, value=self.desc, inline=False)
            else:
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

class CardThreading(object):

    def __init__(self, cards_list, nb_cards):
        self.cards_list = cards_list
        self.nb_cards = nb_cards

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        for i in range(self.nb_cards):
            if  i != 0 and i%5 == 0 :
                time.sleep(5)
            rdm = Guess.get_rdm_guess_nb()
            pos = Guess.get_rdm_pos_nb()
            diff = Guess.get_rdm_diff_nb()
            self.cards_list.append({'card' : Cards.get_random_card(), 'rdm' : rdm, 'pos' : pos, 'diff' : diff})
