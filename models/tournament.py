
from config import CHALLONGE_TOKEN
import requests



class Tournament():

    def __init__(self,ctx ,members):

        self.url = ""

        self.members = members
        self.ctx = ctx
        self.challonge_url =f"https://appez@api.challonge.com/v1/tournaments/"


    def create_tournament(self):

        HEADERS = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",

        }

        data = {
            "name" : "Playing room online tournament",
            "tournament_type" : "swiss",
            "open_signup" : "False",
            "private"  : "True"
        }
        params = {
            "api_key" : f"{CHALLONGE_TOKEN}"
        }

        response = requests.post(
            self.challonge_url,
            headers=HEADERS,
            json=data,
            params=params
        )
        
        print(response)

    def get_tournament(self):
        HEADERS = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            
        }


        params = {
            "api_key" : f"{CHALLONGE_TOKEN}"
        }

        response = requests.get(
            self.challonge_url,
            headers=HEADERS,
            params=params
        )
        
        print(response)

    def delete_tournament(self):
        HEADERS = {
            "Content-Type": "application/json",
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            
        }

        params = {
            "api_key" : f"{CHALLONGE_TOKEN}"
        }

        response = requests.delete(
            self.challonge_url+"awhq8wgv",
            headers=HEADERS,
            params=params
        )
        

    def start(self):
        self.create_tournament()

