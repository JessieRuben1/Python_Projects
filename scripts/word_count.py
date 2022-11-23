"""
Ask the user what's on their mind. Then after the user responds, 
count the number of words in the sentence and print that as an output.
"""

ask = input("What's on your mind? ")
ask = ask.strip()
word_count = len(ask)
print("WOW! You used " + str(word_count) + " letters to tell me about your day")