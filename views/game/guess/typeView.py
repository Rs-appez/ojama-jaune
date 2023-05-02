from discord import ButtonStyle
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
                if self.current_view.guess.check_type(self.type_card,self.current_view.cat) : self.style = ButtonStyle.green
                else : self.style = ButtonStyle.danger

                for btn in self.current_view.children:
                    btn.disabled = True
                await interaction.response.edit_message(view=self.current_view)
                await self.current_view.guess.finish()

    __card_types = ["monster","spell","trap"]
    __spell_types = ["normal","continuous","equip","field","quick-play","ritual"]
    __trap_types = ["normal","continuous","counter"]

    def __init__(self,guess,cat = ""):
        self.guess = guess
        self.click=False
        self.cat = cat
        super().__init__()

        if cat == "spell":
            self.__init_button(self.__spell_types)
        elif cat == "trap":
            self.__init_button(self.__trap_types)
        else :
            self.__init_button(self.__card_types)

    def __init_button(self,list):
        for type in list:
            button = self.Button_type(type,self)
            self.add_item(button)

