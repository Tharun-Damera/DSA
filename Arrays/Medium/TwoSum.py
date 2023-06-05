'''
	Two Sum : Check if a pair with given sum exists in Array

'''

# 1. Brute Force 

def two_sum(arr, summ):

	n = len(arr)

	for i in range(n):
		for j in range(i+1, n):

			if arr[i] + arr[j] == summ:
				return i, j

	return -1, -1

'''
	Time Complexity: O() 
	Space Complexity: O()

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]
summ = int(input('Enter the sum value: '))

e1, e2 = two_sum(arr, summ)

print('\narr:', arr)
print(f'arr[{e1}] + arr[{e2}] = {summ}')
