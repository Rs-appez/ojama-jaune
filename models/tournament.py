
import json
from operator import index
from config import CHALLONGE_TOKEN, CATEGORY_TOURNAMENT_ID
import requests
from nextcord import CategoryChannel


class Tournament():

    _challonge_url = "https://challonge.com/fr/"
    __challonge_api_url =f"https://appez@api.challonge.com/v1/tournaments"
    __api_key = CHALLONGE_TOKEN

    _header = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        }

    __params = {
            "api_key" : f"{__api_key }"
        }

    def __init__(self,ctx ,duelists):

        self.url = ""

        self.duelists = duelists
        self.participants:dict = {}
        self.ctx = ctx
        
        category = [c for c in ctx.guild.categories if c.id == CATEGORY_TOURNAMENT_ID]
        self.category = category[0]
        


    async def create_tournament(self):


        data = {
            "name" : "Playing room online tournament",
            "tournament_type" : "swiss",
            "open_signup" : "False",
            "private"  : "True",
            "game-id" : 45,
            "tournament[game_name]" : "Yu-Gi-Oh!",
        }

        response = requests.post(
            Tournament.__challonge_api_url+".json",
            headers=Tournament._header,
            json=data,
            params=Tournament.__params
        )
        
        if(response.status_code == 200):
            self.url = response.json()['tournament']["url"]
            if (await self.add_members() == 200):
                await self.ctx.send(f"Tournoi crée : {Tournament._challonge_url+self.url} ")
            else :
                await self.ctx.send("Error ajout membre")
        else : 
            await self.ctx.send("Error")


    async def add_members(self):

        participants = []

        for duelist in self.duelists:
            name = duelist.nick or duelist.name
            participants.append({"name" : name })


        data = {
            "participants" : participants,
        }
       

        response = requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/participants/bulk_add.json",
            headers=Tournament._header,
            json=data,
            params=Tournament.__params
        )


        return response.status_code

    def get_participant(self):

        response = requests.get(
        Tournament.__challonge_api_url+f"/{self.url}/participants.json",
        headers=Tournament._header,
        params=Tournament.__params
        )

        if response.status_code ==200:
            
            for index,participant in enumerate( response.json()):
                self.participants[self.duelists[index].name] = participant["participant"]["id"]

        
    def matches(self, duelist_id= None):
        param = Tournament.__params
        param['state'] = 'open'
        if duelist_id:
            param['participant_id'] = duelist_id
        response = requests.get(
            Tournament.__challonge_api_url+f"/{self.url}/matches.json",
            headers=Tournament._header,
            params=param
        )
        if response.status_code == 200:
            return response
    
    async def create_vocal(self):
        matches = self.matches()
        
        for index,m in enumerate(matches.json()):
            cat = await self.category.create_voice_channel(f'Table {index+1}')
            
    
    async def move_player(self):
        matches = self.matches()
        mydict = self.participants
        channels = [x for x in self.category.channels if x.name.startswith('Table')]
        print(channels)
        
        for index, m in enumerate(matches.json()):
            player1 = list(mydict.keys())[list(mydict.values()).index(m['match']['player1_id'])]
            player2 = list(mydict.keys())[list(mydict.values()).index(m['match']['player2_id'])]
            for d in self.duelists:
                if d.name == player1 or d.name == player2:
                    await d.edit(voice_channel = channels[index])
            
            
    async def start_tournament(self):
        requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/participants/randomize.json",
            headers=Tournament._header,
            params=Tournament.__params
        )

        response = requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/start.json",
            headers=Tournament._header,
            params=Tournament.__params
        )

        self.get_participant()
        
        if(response.status_code == 200):
            await self.ctx.send("Tournoi demarré ! ")
            # créer le nombre de channel vocaux / match
            # Bouger les participants dans leurs matchs / channel vocal
            await self.create_vocal()
            await self.move_player()
                
                
        else : 
            await self.ctx.send("Error")

    async def set_win(self, winner, w, l) :
        winner_id = self.participants[winner.name]

        
        match = self.matches(winner_id)
        match_id = match.json()[0]["match"]["id"]


        match_player1_id = match.json()[0]["match"]["player1_id"]


        data = {
            "match": {
                "winner_id" : winner_id
            }
        } 

        if winner_id == match_player1_id:
            data["match"]["scores_csv"] = f"{w}-{l}"
        else:
            data["match"]["scores_csv"] = f"{l}-{w}"

        print(data)

        response = requests.put(
            Tournament.__challonge_api_url+f"/{self.url}/matches/{match_id}.json",
            headers=Tournament._header,
            params= Tournament.__params,
            json=data
        )

        if(response.status_code == 200):
            await self.ctx.send(f"gg {winner.mention}")

        else:
            await  self.ctx.send(f"erreur :/")

        print(response.json())


    @staticmethod
    async def get_tournament() -> json:

        response = requests.get(
            Tournament.__challonge_api_url+".json",
            headers=Tournament._header,
            params=Tournament.__params
        )
        
        return response.json()

    @staticmethod
    async def delete_tournament( url,ctx):

        response = requests.delete(
            Tournament.__challonge_api_url+f'/{url}',
            headers=Tournament._header,
            params=Tournament.__params
        )

        if(response.status_code == 200):
            await ctx.send("Tournoi delete")
        else :
            await ctx.send("Error")
    
    @staticmethod
    async def dell_all_tournament(ctx):

        tournaments =   await Tournament.get_tournament()

        for tournament in tournaments:
            url = tournament['tournament']["url"]
            await Tournament.delete_tournament(url,ctx)

    async def dell_vocal(self, ctx):
        categories = self.ctx.guild.categories            
        category = [c for c in categories if c.id == CATEGORY_TOURNAMENT_ID]
        for c in category[0].channels:
            if c.name.startswith("Table"):
                await c.delete()

    async def start(self):
        await self.create_tournament()

