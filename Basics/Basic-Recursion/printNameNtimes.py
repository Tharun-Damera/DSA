'''
	Print Name N times using Recursion

'''

def print_name_Ntimes(i, n):

	if i == n:
		return 

	print('Tharun')
	print_name_Ntimes(i+1, n)


n = int(input("Enter n value: "))
print_name_Ntimes(0, n)


'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''
