from views.game.battle.registerView import RegisterView
import asyncio

class BattleGuess():

    def __init__(self,author, game_channel,emojis) -> None:
        self.channel = game_channel 
        self.emojis = emojis
        self.players = []
        self.author = author

    async def setup(self):
        msg = await self.channel.send('Player : \npersonne 😭')
        await self.channel.send('Join the party !',view=RegisterView(self.players,self.emojis["aqua"],msg))
        await self.author.send('test')
