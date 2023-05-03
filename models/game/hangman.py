from views.game.hangman.letter_view import Letter_view
from views.game.reload_view import ReloadView

class Hangman():
    __letter = "abcdefghijklmnopqrstuvwxyz"
    __hangman = [
                   "            \n\n\n\n\n\n   ",
                   "            \n\n\n\n\n\n/-\\   ",
                   "            \n\n\n\n\n |\n/-\\   ",
                   "            \n\n\n\n |\n |\n/-\\   ",
                   "            \n\n\n |\n |\n |\n/-\\   ",
                   "            \n\n |\n |\n |\n |\n/-\\   ",
                   "            \n _______\n |\n |\n |\n |\n/-\\   ",
                   "            \n _______\n |     |\n |\n |\n |\n/-\\   ",
                   "            \n _______\n |     |\n |     O\n |\n |\n/-\\   ",
                   "            \n _______\n |     |\n |     O\n |    /|\\\n |\n/-\\   ",
                   "            \n _______\n |     |\n |     O\n |    /|\\\n |    / \\\n/-\\   "]
    __error = 0
    __game_msg = None
    __vowel_msg = None
    __consonant_msg = None

    def __init__(self, word : str,interaction,gm ,item = None):
        self.word = word.lower()
        self.gm = gm
        self.item = item
        self.interaction = interaction
        self.__init_word()

        self.vowel_view = None
        self.consonant_view = None

    def __init_word(self):
        self.game_word = ""
        for l in self.word:
            if l in self.__letter:
                self.game_word+="_"
            elif  l == "_" : self.game_word+=" "
            else: self.game_word+=l

    async def start(self):
        if not self.__game_msg:
            self.__game_msg = await self.interaction.send(self.dispaly())
            self.__vowel_msg = await self.interaction.channel.send("Voyelle :",view=Letter_view(self,True))
            self.__consonant_msg = await self.interaction.channel.send("Consonne :",view=Letter_view(self,False))
    def dispaly(self):
        return f"```-> {self.game_word}\n{self.__hangman[self.__error]}```"
    
    async def add_error(self):
        self.__error+=1 
        if self.__error >= 10:
            await self.finish(False)


    async def add_letter (self,letter):
        for index,l in enumerate(self.word):
            if l == letter :  self.game_word =  self.game_word[:index] + l + self.game_word[index+1:]
        if not "_" in self.game_word:
            await self.finish(True)

    async def check_letter(self, letter : str):
        succes = letter.lower() in self.word
        if succes :
            await self.add_letter(letter.lower())
        else :
            await self.add_error()
        await self.__game_msg.edit(self.dispaly())
        return succes
    
    async def finish(self,win):
        
        for button in self.vowel_view.children:
            button.disabled = True

        for button in self.consonant_view.children:
            button.disabled = True

        await self.__consonant_msg.edit(view=self.consonant_view)
        await self.__vowel_msg.edit(view=self.vowel_view)

        if win : await self.interaction.channel.send("https://tenor.com/view/sweet-victory-spongebob-sweet-sweet-victory-superbowl-gif-13419935")
        else : 
            await self.interaction.channel.send("https://tenor.com/view/dead-gif-18865199")
            await self.interaction.channel.send(f"Le mot était : {self.word}")

        if self.item : await self.interaction.channel.send(self.item)
        await self.interaction.channel.send(view=ReloadView(self.gm))

        self.vowel_view.stop()
        self.consonant_view.stop()
