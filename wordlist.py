import random

class WordList:

    _words=["rainbow","camel", "jazz", "grass", "follow","Hulk"]

    def get_word(self):
        if self._words:
            return random.choice(self._words)
        else:
            raise ValueError("Word list is empty. Please add words first.")
    