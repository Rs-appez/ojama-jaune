
from typing import Optional, Union
from discord import ButtonStyle
from nextcord.emoji import Emoji
from nextcord.enums import ButtonStyle
from nextcord.partial_emoji import PartialEmoji
from nextcord.ui import View , Button
GAME_EMOJI = None
class TypeView(View):

    class Button_type(Button):

        def __init__(self, type, current_view):
            self.type_card = type
            self.curent_view = current_view
            super().__init__(style=ButtonStyle.primary,emoji=current_view.guess.game_emojis[type])

    __card_types = ["monster_effect","spell","trap"]

    def __init__(self,guess,):
        self.guess = guess
        super().__init__(timeout=None)

        self.__init_button()

    def __init_button(self):
        for type in self.__card_types:
            button = self.Button_type(type,self)
            self.add_item(button)

