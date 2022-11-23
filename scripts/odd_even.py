def odd_even(n):
    """
    It takes a number as an input and returns whether the number is even or odd.
    
    :param n: The number you want to check if it's odd or even
    :return: The number you have entered is EVEN
    """
    if n % 2 == 0:
        return "The number you have entered is EVEN ", n
    else:
        return "The number you have entered is ODD ", n

# Asking the user to input a number and then it is checking whether the number is odd or even.
print('Welcome this program checks whether a number is odd or even \n')
x = int(input("Enter a number from 1 to 1000: "))

y = odd_even(x)
print(y)