#Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""
def unique_list(l):
    x = []
    for item in l:
        if item not in x:
            x.append(item)
    return x    

unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
"""

def unique_list(l):
    # Also possible to use list(set())
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])