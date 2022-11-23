def fib(max):
    """
    It's a function that returns a generator object that yields the next Fibonacci number each time it's
    called
    
    :param max: The maximum value of the Fibonacci number to generate
    """
    f1, f2 = 0, 1
    while f1 < max:
        yield f1
        f1, f2 = f2, f1 + f2

print(sum(filter(lambda n: n % 2 == 0, fib(4000000))))

# sum = 0
# f1, f2 = 0, 1
# while f2 < 4000000:
#     if f2 % 2 == 0:
#         sum += f2
#     f1, f2 = f2, f1 + f2
# print(sum)

# Find the sum of all the even-valued
# terms in the Fibonacci sequence which
# do not exceed given limit.

# Returns sum of even Fibonacci numbers which
# are less than or equal to given limit.
# def evenFibSum(limit) :
# 	if (limit < 2) :
# 		return 0

# 	# Initialize first two even prime numbers
# 	# and their sum
# 	ef1 = 0
# 	ef2 = 2
# 	sm= ef1 + ef2
	
# 	# calculating sum of even Fibonacci value
# 	while (ef2 <= limit) :

# 		# get next even value of Fibonacci
# 		# sequence
# 		ef3 = 4 * ef2 + ef1

# 		# If we go beyond limit, we break loop
# 		if (ef3 > limit) :
# 			break

# 		# Move to next even number and update
# 		# sum
# 		ef1 = ef2
# 		ef2 = ef3
# 		sm = sm + ef2
	
# 	return sm

# # Driver code
# limit = 4000000
# print(evenFibSum(limit))

# This code is contributed by Nikita Tiwari.
