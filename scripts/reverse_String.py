def reverse_string(s):
    words = s.split(" ")
    rev_sentece = " ".join(reversed(words))
    return rev_sentece


s = input("Enter a sentence: ")

print(reverse_string(s),end = "")