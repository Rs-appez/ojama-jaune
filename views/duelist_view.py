

import nextcord

class DuelistView(nextcord.ui.View):

    def __init__(self,ctx):
        self.ctx = ctx
        super().__init__(timeout=None)


    async def start(self, interaction : nextcord.Interaction):
       await self.ctx.send(content="go !")



    @nextcord.ui.button(label="confirmer",emoji="✅" ,style=nextcord.ButtonStyle.primary)
    async def participate_button(self,button,interaction):
        await self.start(interaction)
