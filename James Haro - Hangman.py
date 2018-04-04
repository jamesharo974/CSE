import random
import string
"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letter guessed
4. Reveal letters already guessed
5. Create win condition
"""

tries = 21

word_bank = ["southern wall", "motorsport", "ninja turtles", "expensive water", "over priced pencils",
             "fire extinguisher",   "wallpaper", "geometry", "west carolina", "lava lamp"]

word_picked = (random.choice(word_bank))
letters_guessed = []
ranged_word = len(word_picked)
guess = ""
correct = list(word_picked)



while tries > 0:
    output = []
    for letter in word_picked:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print(output)
    tries -= 1
    print("You have %s tries left." %tries)

    current_guess = input("Guess a letter: ")
    letters_guessed.append(current_guess)
    print(letters_guessed)

    if tries == 0:
        print("You Lost")

    if output == correct:
        print("You Win")







