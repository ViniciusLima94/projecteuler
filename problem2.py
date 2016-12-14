# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Receive the index of the number in the series
def fibonacci(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

# The sequence generated by the fibonacci method: 1, 1, 2, 3, 5, 8, 13, 21, 34...
# Notice that beginning with index 0, the even elements have indexes tha follows the aritimetic progression 2, 5, 8...
# So beginning in index 2, we can increase it by 3 in each step
idx = 2
fib = 0 # Store fibonacci numbers.
sum = 0 # Store sum of even fibonacci numbers.

while fib < 4e6:
	sum += fib
	fib = fibonacci(idx)
	idx += 3

print sum
