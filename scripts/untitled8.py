# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:42:52 2021

@author: admin
"""

def canBeTypedWords( text, brokenLetters):
    """
    If the length of the intersection of the set of letters in a word and the set of broken letters is
    greater than 0, then the word can't be typed. 
    
    The function returns the number of words that can't be typed
    
    :param text: a string of words separated by spaces
    :param brokenLetters: a string of letters that are broken on the keyboard
    :return: The number of words that cannot be typed with the broken letters.
    """
    t=set(brokenLetters)
    b=0
    for i in text.split():
        if (len(set(i) & t) >0):
                b=b+1
    return len(text.split())-b

# This is a way to run the code in the file.
if __name__ == '__main__':
    text = "Hello, darkness my old friend!"
    letters = ['e', 'i', 'h', 'l', 'o']
    print(canBeTypedWords(text, letters))
        

