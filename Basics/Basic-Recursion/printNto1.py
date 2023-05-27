'''
	Print N to 1 using Recursion

'''

def print_N_to_1(i, n):

	if i == 0:
		return 

	print(i)
	print_N_to_1(i-1, n)


n = int(input("Enter n value: "))
print_N_to_1(n, n)


'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''
