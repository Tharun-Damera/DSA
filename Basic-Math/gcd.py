'''
	Find GCD of two numbers

'''
# I. Naive approach 

def gcdI(a, b):

	for i in range(1, min(a, b)+1):
		if a % i == 0 and b % i == 0:
			ans = i

	return ans

'''
	Time Complexity : O(min(a, b))
	Space Complexity : O(1)

'''


# II. Better Approach using Euclidean Theorem (Recursive)

def gcdII(a, b): 
	if b == 0:
		return a

	return gcdII(b, a % b)

'''
	Time Complexity : O(log(min(a, b)))
	Space Complexity : O(log(min(a, b))) -> due to recursion stack

'''

# III. Optimized Approach (Iterative)

def gcdIII(a, b):

	while a > 0 and b > 0:
		if a > b:
			a = a % b
		else:
			b = b % a

	if a == 0:
		return b
	else:
		return a


'''
	Time Complexity : O(log(min(a, b)))
	Space Complexity : O(1) 

'''


a = int(input('Enter a value: '))
b = int(input('Enter b value: '))
print(f'GCD of {a} and {b} is {gcdIII(a, b)}')

