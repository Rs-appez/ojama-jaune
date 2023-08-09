from discord import ButtonStyle
from nextcord.ui import View, button


class StarterView(View):
    def __init__(self,game) -> None:

        self.game = game
        super().__init__()

    @button(label="START !",style=ButtonStyle.primary,emoji="▶️")
    async def reload(self,button,interaction):
       
        button.disabled = True
        await interaction.response.edit_message(view=self)
        await self.game.start()
    
