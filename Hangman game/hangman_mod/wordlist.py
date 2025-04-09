import random

class WordList:

    movies = [
    "Inception", "Titanic", "Gladiator", "Whiplash", "Interstellar",
    "The Matrix", "Forrest Gump", "The Godfather", "Parasite", "Pulp Fiction"
    ]
    
    fruits = [
        "Apple", "Banana", "Cherry", "Date", "Elderberry",
        "Fig", "Grape", "Mango", "Orange", "Pineapple"
    ]
    
    countries = [
        "India", "Brazil", "Canada", "France", "Germany",
        "Japan", "Mexico", "Nigeria", "Spain", "Australia"
    ]
    
    word_categories = {
    "1": movies,
    "2": fruits,
    "3": countries} # category list (key=index, value= themed word list)


    def get_word(self,category: str):
        category = category.lower()
        word_categories=self.word_categories
        if category in word_categories:
            return random.choice(word_categories[category]).lower()
        else:
            raise ValueError(f"Invalid category: '{category}'. Choose from {list(word_categories.keys())}")
    