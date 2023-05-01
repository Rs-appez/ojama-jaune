
from discord import ButtonStyle
from nextcord.ui import View, Button

class Letter_view(View):

    class Button_letter(Button):

        def __init__(self, letter ,current_view):
            self.letter = letter
            self.current_view = current_view
            self.click = False
            super().__init__(label=letter,style=ButtonStyle.primary)

        async def callback(self,interaction):
            if not self.click:
                self.click = True
                self.disabled=True
                
                if await self.current_view.hangman.check_letter(self.letter) : self.style = ButtonStyle.green
                else : self.style = ButtonStyle.danger

                await interaction.response.edit_message(view=self.current_view)

    # __letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __letter_vowel = "AEIOUY"
    __letter_consonant = "BCDFGHJKLMNPQRSTVWXZ"
    def __init__(self, hangman , vowel):
        self.hangman = hangman
        super().__init__(timeout=None)
        self.__init_button(vowel)

        if vowel : hangman.vowel_view = self
        else : hangman.consonant_view = self

    def __init_button(self,vowel):
        if vowel : letters = self.__letter_vowel
        else : letters = self.__letter_consonant
        for letter in letters:
            button = self.Button_letter(letter,self)
            self.add_item(button)


    
        