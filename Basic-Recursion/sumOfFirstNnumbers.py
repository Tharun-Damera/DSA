'''
	Sum of first N Natural Numbers
	Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

'''

def sum_of_first_N_numbers(n):

	if n == 1:
		return 1

	return n + sum_of_first_N_numbers(n-1)


n = int(input("Enter n value: "))
ans = sum_of_first_N_numbers(n)
print(f'The sum of {n} numbers is {ans}.')

'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''