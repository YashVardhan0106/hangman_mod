

class Game:
    

    def __init__(self,chosen_word):
        self.chosen_word=chosen_word
        self.blank_list=list("_"*len(self.chosen_word))
        self.update_display=0
        self.game_graphics=['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    =========''']
    
    

    def making_a_guess(self, guess):
        if guess in self.chosen_word:
            for index, letter in enumerate(self.chosen_word):
                if letter == guess:
                    self.blank_list[index] = guess  # Update the blank list with correct letters
        else:
            self.update_display += 1  # Increment when the guess is incorrect

    def play(self):
        print(self.game_graphics[self.update_display])
        guess = input(f"Welcome to Hangman.\n{''.join(self.blank_list)}\nMake a guess? ")
        self.making_a_guess(guess)
        print(self.game_graphics[self.update_display])
        print(''.join(self.blank_list))

        while self.update_display < 6:
            if "".join(self.blank_list) == self.chosen_word:  # Convert blank_list to string before comparison
                print("YOU WIN!")
                return
            guess = input("Make another guess? ")
            self.making_a_guess(guess)
            print(self.game_graphics[self.update_display])
            print(''.join(self.blank_list))

        if self.update_display == 6:
            print("GAME OVER.")