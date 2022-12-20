import json

class OpDeck():

    def __init__(self, data :json) -> None:
        self.deck = json.loads(data)[1:]
    
    def convert(self):

        self.deck_converted = ""

        cards = []
        copies = []


        for e in self.deck:
            if e in cards:
                copies[cards.index(e)] += 1
            else :
                cards.append(e)
                copies.append(1)
        
        for i,c in enumerate(cards):

            self.deck_converted += f"{copies[i]}X{c}\n"

        return self.deck_converted