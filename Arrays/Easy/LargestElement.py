'''
	Find the Largest element in an array
	Problem Statement: Given an array, we have to find the largest element in the array.
'''

def find_max(arr):
	n = len(arr)
	max_value = arr[0]

	for num in arr:
		if num > max_value:
			max_value = num

	return max_value


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

res = find_max(arr)
print(f'Max Value of {arr} is {res}')


'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''