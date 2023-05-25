'''
	Print 1 to N using Recursion

'''

def print_1_to_N(i, n):

	if i > n:
		return 

	print(i)
	print_1_to_N(i+1, n)


n = int(input("Enter n value: "))
print_1_to_N(1, n)


'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''
