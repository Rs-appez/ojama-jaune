
import json
import re
from config import CHALLONGE_TOKEN
import requests



class Tournament():

    _challonge_url = "https://challonge.com/fr/"
    __challonge_api_url =f"https://appez@api.challonge.com/v1/tournaments"
    __api_key = CHALLONGE_TOKEN

    def __init__(self,ctx ,members):

        self.url = ""

        self.members = members
        self.ctx = ctx
        


    async def create_tournament(self):

        HEADERS = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        }

        data = {
            "name" : "Playing room online tournament",
            "tournament_type" : "swiss",
            "open_signup" : "False",
            "private"  : "True",
            "game-id" : 45,
            "tournament[game_name]" : "Yu-Gi-Oh!",
        }
        params = {
            "api_key" : f"{Tournament.__api_key }"
        }

        response = requests.post(
            Tournament.__challonge_api_url+".json",
            headers=HEADERS,
            json=data,
            params=params
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

        for member in self.members:
            participants.append({"name" : member})

        HEADERS = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        }

        data = {
            "participants" : participants,
        }
        params = {
            "api_key" : f"{Tournament.__api_key }"
        }

        response = requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/participants/bulk_add.json",
            headers=HEADERS,
            json=data,
            params=params
        )

        requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/participants/randomize.json",
            headers=HEADERS,
            params=params
        )

        return response.status_code

    @staticmethod
    async def get_tournament() -> json:
        HEADERS = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            
        }


        params = {
            "api_key" : f"{Tournament.__api_key }"
        }

        response = requests.get(
            Tournament.__challonge_api_url+".json",
            headers=HEADERS,
            params=params
        )
        
        return response.json()

    @staticmethod
    async def delete_tournament( url,ctx):
        HEADERS = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            
        }

        params = {
            "api_key" : f"{Tournament.__api_key}"
        }

        response = requests.delete(
            Tournament.__challonge_api_url+f'/{url}',
            headers=HEADERS,
            params=params
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


    async def start(self):
        await self.create_tournament()

