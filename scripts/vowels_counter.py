# Counting the number of vowels in a word.
word = input("Enter a word: ").lower()
counter = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for i in vowels:
    if i in word:
        counter += 1
print(str(counter) , word)