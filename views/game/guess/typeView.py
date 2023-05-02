
from typing import Optional, Union
from discord import ButtonStyle
from nextcord.emoji import Emoji
from nextcord.enums import ButtonStyle
from nextcord.ui import View , Button
class TypeView(View):

    class Button_type(Button):

        def __init__(self, type, current_view):
            self.type_card = type
            self.current_view = current_view
            super().__init__(label=type.upper(),style=ButtonStyle.primary,emoji=current_view.guess.game_emojis[type])

        async def callback(self,interaction):
            if not self.current_view.click:
                self.current_view.click = True
                if self.current_view.guess.check_type(self.type_card) : self.style = ButtonStyle.green
                else : self.style = ButtonStyle.danger

                for btn in self.current_view.children:
                    btn.disabled = True
                await interaction.response.edit_message(view=self.current_view)
                await self.current_view.guess.finish()

    __card_types = ["monster","spell","trap"]

    def __init__(self,guess,):
        self.guess = guess
        self.click=False
        super().__init__(timeout=None)

        self.__init_button()

    def __init_button(self):
        for type in self.__card_types:
            button = self.Button_type(type,self)
            self.add_item(button)

