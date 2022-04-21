

import nextcord

from models.tournament import Tournament

class DuelistView(nextcord.ui.View):

    def __init__(self,ctx, tournament : Tournament):
        self.ctx = ctx
        self.tournament = tournament
        super().__init__(timeout=None)


    async def start(self):
       await self.tournament.start()



    @nextcord.ui.button(label="confirmer",emoji="✅" ,style=nextcord.ButtonStyle.primary)
    async def participate_button(self,button,interaction):
        await self.start()
