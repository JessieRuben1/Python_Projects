import random
from words import words
import string

def valid_word(words):
    """
    It takes a list of words as an argument, chooses a random word from the list, and returns the word
    if it doesn't contain a dash or a space. If it does contain a dash or a space, it chooses another
    random word from the list and checks that one. It keeps doing this until it finds a word that
    doesn't contain a dash or a space
    
    :param words: a list of words
    :return: A random word from the list of words.
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word)  #letters in a word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    #getting user input
    while len(word_letters) >0:
        #letters used
        print("you have used these letters: "," ".join(used_letters))

        #What the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word : ', ' '.join(word_list))
        user_letter = input("Guess the letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)


        elif user_letter in used_letters:
            print("Letter alredy used, try again")

        else:
            print("Invalid character")



hangman()

    