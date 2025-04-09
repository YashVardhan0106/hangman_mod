# Hangman_mod Package

## Overview

The `hangman_mod` package is a modular Python package designed for a Hangman game. It contains three main modules:

- `user.py` - Handles user-related functionality.
- `wordlist.py` - Stores and retrieves words for the game.
- `game.py` - Implements the Hangman game logic.

## Installation

To use the package, clone the repository and ensure that Python is installed.

```sh
pip install -r requirements.txt  # If dependencies exist
```

## Usage

Run the game using the following command:

```sh
python -m hangman_mod.main
```

## Package Structure

```
hangman_game/
|──hangman_mod/
  ├── __init__.py  # Package initializer
  ├── user.py      # User management
  ├── wordlist.py  # Word storage
  ├── game.py      # Game logic
├── main.py      # Entry point
```



