#Python program for a simple calculator using classes
#Calculator performs addition, subtraction, multiplication and, division
# It adds two numbers together.
class Calculator():
    def __init__(self, number1, number2):       #Find a way to add more numbers
        """
        It adds two numbers together.
        
        :param number1: The first number to be added
        :param number2: The second number to be added
        """
        self.number1 = number1
        self.number2 = number2

    def add(self):
        """
        It adds the two numbers
        :return: The sum of the two numbers.
        """
        return self.number1 + self.number2

    def minus(self):
        """
        If the first number is greater than the second number, return the difference between the two
        numbers. Otherwise, return an error message
        :return: The difference between the two numbers.
        """
        if self.number1 > self.number2:
            return self.number1 - self.number2
        else:
            return "Error"
        
        
    def multiple(self):
        """
        It returns the product of the two numbers.
        :return: The result of the multiplication of the two numbers.
        """
        
        return self.number1 * self.number2 
    
    def division(self):
        """
        It returns the result of dividing number1 by number2, or an error if number2 is zero
        :return: The result of the division operation.
        """
        try:
            return self.number1 // self.number2
        except ZeroDivisionError as e:
            return e



# Creating an instance of the class Calculator.
problem1 = Calculator(10, 5)

# Calling the functions in the class.
print(problem1.add())
print(problem1.division())
print(problem1.minus())
print(problem1.multiple())