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
            await self.current_view.btn_callback(interaction,self)
            
    class Button_level(Button):

        def __init__(self, type, current_view,val):
            self.type_card = val
            self.current_view = current_view
            super().__init__(label=val,style=ButtonStyle.primary,emoji=current_view.guess.game_emojis[type])

        async def callback(self,interaction):
            await self.current_view.btn_callback(interaction,self)
            
    

    __card_types = ["monster","spell","trap"]
    __spell_types = ["normal","continuous","equip","field","quick-play","ritual"]
    __trap_types = ["normal","continuous","counter"]
    __attribute_types = ["light","dark","water","fire","earth","wind","divine"]
    __race_types1 = ["aqua","beast","beast-warrior","creator god","cyberse","dinosaur","divine-beast","dragon","fairy","fiend",
                     "fish","illusionist","insect","machine","plant","psychic","pyro","reptile","rock","sea serpent","spellcaster",
                     "thunder","warrior","winged beast","wyrm"]
    __race_types2 = ["zombie"]
    __monster_card_types = ["normal ","effect","tuner","fusion","synchro","xyz","link","ritual ","pendulum"]
    __level_monster = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    __linkrating_monster = [1,2,3,4,5,6,7,8]
    
    def __init__(self,guess,cat = "",first_view= None):
        self.guess = guess
        self.click=False
        self.cat = cat
        self.first_view = first_view
        self.second_view = None
        if first_view:
            self.first_view.__add_second_view(self)
        super().__init__(timeout=10)

        if cat == "spell":
            self.__init_button_type(self.__spell_types)
        elif cat == "trap":
            self.__init_button_type(self.__trap_types)
        elif cat == "attribute":
            self.__init_button_type(self.__attribute_types)
        elif cat == "race1":
            self.guess.first_view = self
            self.__init_button_type(self.__race_types1)
        elif cat == "race2":
            self.__init_button_type(self.__race_types2)
        elif cat in ["level","rank"]:
            self.__init_button_val(self.__level_monster)
        elif cat == "link":
            self.__init_button_val(self.__linkrating_monster)
        elif cat == "type_monster_card":
            self.__init_button_type(self.__monster_card_types)
        else :
            self.__init_button_type(self.__card_types)

    def __init_button_type(self,list):
        for type in list:
            button = self.Button_type(type,self)
            self.add_item(button)

    def __init_button_val(self,list):
        for val in list:
            button = self.Button_level(self.cat,self,val)
            self.add_item(button)

    async def btn_callback(self,interaction,button):

        if not self.click:
            self.click = True
            if self.guess.check_type(button.type_card,self.cat) : button.style = ButtonStyle.green
            else : button.style = ButtonStyle.danger

            for btn in self.children:
                btn.disabled = True
            await interaction.response.edit_message(view=self)

            if self.second_view:
                for btn in self.second_view.children:
                    btn.disabled = True
                await self.guess.second_msg.edit(view=self.second_view)

            elif self.first_view:
                for btn in self.first_view.children:
                    btn.disabled = True
                await self.guess.first_msg.edit(view=self.first_view)

            await self.guess.finish()

    def __add_second_view(self,second_view):
        self.second_view = second_view
    
    async def on_timeout(self):
        for btn in self.children:
                btn.disabled = True
        if self.first_view:
            await self.guess.first_msg.edit(view=self.first_view)
        elif self.second_view:
            for btn in self.second_view.children:
                btn.disabled = True
            await self.guess.second_msg.edit(view=self.second_view)
        else :
            await self.guess.msg.edit(view=self)
        
        return await super().on_timeout()
