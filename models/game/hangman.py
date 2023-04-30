class Hangman():
    _hangman = [
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
    error = 0

    def dispaly(self):
        return self._hangman[self.error]
    def add_error(self):
        self.error+=1 