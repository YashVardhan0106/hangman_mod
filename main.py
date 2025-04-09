

# Import necessary modules from the package
from hangman_mod.user import User
from hangman_mod.wordlist import WordList
from hangman_mod.game import Game

def main():
    user=User()
    user.set_name(input("Enter your Name?"))
    user.greet()
    
    print("let's Begin!")

    words=WordList()
    theme=input(f"Select your theme: 1. Movies
                                     2. Fruits
                                     3. Countries")
    game=Game(words.get_word(theme))
    game.play()

if __name__=="__main__":
    main()

    
