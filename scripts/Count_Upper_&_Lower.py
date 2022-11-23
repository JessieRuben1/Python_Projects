"""
Counts the number of Upper case letters and Lower case letters in a string and displays the 
result.
"""

def up_low(s):
    """
    The function takes a string as input, and returns the number of upper and lower case letters in the
    string
    
    :param s: The string to be checked
    """
    d = {"Upper":0,"Lower":0}
    for c in s:
        if c.isupper():
            d["Upper"]+=1
        elif c.islower():
            d["Lower"]+=1
        else:
            pass
    print("Original String : ", s) 
    print("No. of Upper case characters : ", d["Upper"]) 
    print("No. of Lower case Characters : ", d["Lower"]) 
    

s = input("Enter a sentence: ")
up_low(s)
    
    
