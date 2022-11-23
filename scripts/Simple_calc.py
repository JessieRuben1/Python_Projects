#Python program for a simple calculator using classes
#Calculator performs addition, subtraction, multiplication and, division
class Calculator():
    def __init__(self, number1, number2):       #Find a way to add more numbers
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def minus(self):
        if self.number1 > self.number2:
            return self.number1 - self.number2
        else:
            return "Error"
    def multiple(self):
       return self.number1 * self.number2 
    
    def division(self):
        try:
            return self.number1 // self.number2
        except ZeroDivisionError as e:
            return e



problem1 = Calculator(10, 5)

print(problem1.add())
print(problem1.division())
print(problem1.minus())
print(problem1.multiple())