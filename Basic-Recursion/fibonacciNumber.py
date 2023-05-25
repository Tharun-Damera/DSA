'''
	Print Fibonacci Series up to Nth term
	Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.
'''

# 1. Iterative Approach
def fibonacci(n):

	if n == 0:
		return [0]
	elif n == 1:
		return [0, 1]
	else:
		fib = [0, 1]
		for i in range(2, n+1):
			fib.append(fib[i-1] + fib[i-2])

		return fib

'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> for storing fibonacci series

'''


# 2. Recursive Approach
def fibonacci_II(n):

	if n <= 1:
		return n

	return fibonacci_II(n-1) + fibonacci_II(n-2)

'''
	Time Complexity: O(2^n)
	Space Complexity: O(n) -> due to recursion stack

'''


n = int(input('Enter n value: '))
fib = fibonacci(n)
print(f'Fibonacci series of {n} terms is {fib}.')


print(f'{n}th fibonacci number using recursion: {fibonacci_II(n)}')
