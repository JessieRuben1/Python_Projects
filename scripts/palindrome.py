#check if a string is a palindrome
def palindrome(s):
    s.replace(" ","")
    if s == s[::-1]:
        print("Yes")

input()        
print(palindrome('ten animals i slam in a net'))