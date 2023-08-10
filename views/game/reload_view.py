from discord import ButtonStyle
from nextcord.ui import View, button


class ReloadView(View):
    def __init__(self,gm,game, others = None) -> None:
        self.gm = gm
        self.click = False
        self.game = game
        self.others = others
        super().__init__()

    @button(label="AGAIN !",style=ButtonStyle.primary,emoji="🔁")
    async def reload(self,button,interaction):
        if not self.click:
            self.click = True
            button.disabled = True
            await interaction.response.edit_message(view=self)
            await self.gm.reload(interaction,others=self.others)
    
    async def on_timeout(self) :
        self.clear_items()
        await self.game.reload_msg.edit(content="**GG!**",view=self)
        return await super().on_timeout()