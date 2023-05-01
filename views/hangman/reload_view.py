from typing import Optional
from discord import ButtonStyle
from nextcord.ui import View, button


class ReloadView(View):
    def __init__(self,gm) -> None:
        self.gm = gm
        self.click = False
        super().__init__()

    @button(label="AGAIN !",style=ButtonStyle.primary,emoji="🔁")
    async def reload(self,button,interaction):
        if not self.click:
            self.click = True
            button.disabled = True
            await interaction.response.edit_message(view=self)
            await self.gm.reload(interaction)