# Creating a list of numbers.
nums = [3, 5]

# Setting the variable `result` to 0.
result = 0
# Iterating through the numbers 0 to 999 and adding the numbers that are divisible by 3 or 5 to the
# result.
for i in range(0,1000):
    if i%3 == 0 or i%5 == 0:
        result += i

print(result)