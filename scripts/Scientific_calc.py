import math

#Addition function
def addition(x,y):
    print("\nthe answer is: {}".format(x + y))


#SubtractionFunction
def substraction(x,y):
    print("\nThe answer is: {}".format(x - y))

#Multiplication function
def multiplication(x,y):
    print("\nThe answer is: {}".format(x * y))

#Division function
def divide(x,y):
    try:
        print("\nThe answer is: {}".format(x / y))
    except ZeroDivisionError:
        print("\nThe second value cannot be zero")

#Modulus Function
def modulo_(x,y):
    print("\nThe answer is: {}".format(x % y))

#Raise to power function
def raise_to_pow(x,y):
    print("\nThe answer is: {}".format(math.pow(x, y)))
    
#log function
def logg(x):
    print("\nThe answer is: {}".format(math.log(x, 2)))
#Sine function
def sine(x):
     print("\nThe answer is: {}".format(math.sin(math.radians(x))))

#Cosine function
def cosine(x):
     print("\nThe answer is: {}".format(math.cos(math.radians(x))))

#tangent function
def tann(x):
     print("\nThe answer is: {}".format(math.tan(math.radians(x))))
if __name__ == '__main__':
#while loop for the menu
    while True:
        print("Chose an operation to calculate \n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulus\n5 - Raising to power\n6 - Logarithm\n7 - Sine\n8 - Cosine\n9 - Tangent\n")

        oper = float(input("\nYour operator chosen: "))
        
        #Addition
        if oper == 0:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))

            addition(num1, num2)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break
        
        #Subtraction
        elif oper == 1:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))

            substraction(num1, num2)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break

        #Multiplication
        elif oper == 2:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))  

            multiplication(num1, num2)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break

        #Division
        elif oper == 3:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))  

            divide(num1, num2)
            
            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break
        
        #Modulus
        elif oper == 4:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: ")) 

            modulo_(num1, num2)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break

        
        #Raising to power
        elif oper == 5:
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: ")) 

            raise_to_pow(num1, num2)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break

        #Log
        elif oper == 6:
            print("\n finds the log of a number to base of 2")
            num1 = float(input("Enter a number: "))

            logg(num1)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break

        #Sine
        elif oper == 7:
            num1 = float(input("Enter a number: "))

            sine(num1)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break

        #Cosine
        elif oper == 8:
            num1 = float(input("Enter a number: "))

            cosine(num1)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break

        #Tangent
        elif oper == 9:
            num1 = float(input("Enter a number: "))

            tann(num1)

            back = input("\n Would you like to continue? (y/n) ")
            if back == "y" or back == "Y":
                continue
            else:
                break
        
        else:
            print("\n You have selected an invalid operation: please try again ")
            continue