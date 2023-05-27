'''
	Factorial of a Number : Iterative and Recursive
	Problem Statement: Given a number X,  print its factorial.

'''

def factorial(n):
	if n == 1 or n == 0:
		return 1

	return n * factorial(n-1)


n = int(input("Enter n value: "))
ans = factorial(n)
print(f'The factorial of {n} is {ans}.')

'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''