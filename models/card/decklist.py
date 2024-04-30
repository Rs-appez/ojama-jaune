import requests
import config

class Decklist():

    api_url = config.BACKEND_URL + "decklist/decklisturls/"

    def __init__(self, name,url, post_by ):
        self.url = url
        self.name = name
        self.post_by = post_by

    @staticmethod
    def get_decklist(id):
        response = requests.get(Decklist.api_url + str(id),headers={"Authorization":config.BACKEND_TOKEN})
        if response.status_code == 200:
            response = response.json()
            return Decklist(response['name'],response['url'],response['post_by'])
        else:
            return None
        
    def save(self):
        response = requests.post(Decklist.api_url,headers={"Authorization":config.BACKEND_TOKEN},json={"name":self.name,"url":self.url,"post_by":self.post_by})
        if response.status_code == 200:
            return True
        else:
            return False
