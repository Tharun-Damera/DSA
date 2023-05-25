'''
	Sum of first N Natural Numbers
	Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

'''

def sum_of_first_N_numbers(i, total):

	if i == 0:
		print(total)
		return

	sum_of_first_N_numbers(i-1, total+i)



n = int(input("Enter n value: "))
sum_of_first_N_numbers(n, 0)

'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''