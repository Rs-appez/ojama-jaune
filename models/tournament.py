
import json
from config import CHALLONGE_TOKEN
import requests



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

    def __init__(self,ctx ,members):

        self.url = ""

        self.members = members
        self.ctx = ctx
        


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

        for index,member in enumerate(self.members):
            print(index)
            participants.append({"name" : member})


        data = {
            "participants" : participants,
        }
       

        response = requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/participants/bulk_add.json",
            headers=Tournament._header,
            json=data,
            params=Tournament.__params
        )

        requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/participants/randomize.json",
            headers=Tournament._header,
            params=Tournament.__params
        )

        return response.status_code

    async def get_participant(self):

        response = requests.get(
        Tournament.__challonge_api_url+f"/{self.url}/participants.json",
        headers=Tournament._header,
        params=Tournament.__params
        )

        print(response.json())

    async def start(self):



        response = requests.post(
            Tournament.__challonge_api_url+f"/{self.url}/start.json",
            headers=Tournament._header,
            params=Tournament.__params
        )

        if(response.status_code == 200):
            await self.ctx.send("Tournoi demarré ! ")
        else : 
            await self.ctx.send("Error")



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


    async def start(self):
        await self.create_tournament()

