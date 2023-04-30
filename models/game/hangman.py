class Hangman():
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
    game_msg = None

    def __init__(self, word : str):
        self.word = word.lower()
        

    def dispaly(self):
        return self.__hangman[self.__error]
    
    async def add_error(self):
        self.__error+=1 
        await self.game_msg.edit(f"```{self.dispaly()}```")

    async def check_letter(self, letter : str):
        if letter.lower() in self.word :
            return True
        else :
            await self.add_error()
            return False