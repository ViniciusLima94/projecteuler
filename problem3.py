# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# Generates a list of prime numbers
def isprime(N):
	count = 0
	for i in range(1,N+1):
		if N%i == 0:
			count += 1
	if count == 2:
		return True
	else:
		return False
# Receive size of list, return primes list from  beggining from greater element
def primel(l):
	primes = []
	num = 1
	while len(primes) <= l:
		if isprime(num) == True:
			primes.append( num )
		num += 1
	return primes[::-1]

primes = primel(2000)

for num in primes:
	if 600851475143 % num == 0:
		print num
		break
