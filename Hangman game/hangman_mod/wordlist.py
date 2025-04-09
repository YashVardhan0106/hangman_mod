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
    "movies": movies,
    "fruits": fruits,
    "countries": countries}


    def get_word(self,category: str):
        category = category.lower()
        word_categories=self.word_categories
        if category in word_categories:
            return random.choice(word_categories[category])
        else:
            raise ValueError(f"Invalid category: '{category}'. Choose from {list(word_categories.keys())}")
    