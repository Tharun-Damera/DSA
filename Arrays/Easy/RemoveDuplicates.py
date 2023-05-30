'''
	Remove Duplicates in-place from sorted array

'''

#1. Brute Force
def remove_duplicates(arr):

	unique = set()

	for num in arr:
		unique.add(num)

	size = len(unique)
	i = 0
	for num in unique:
		arr[i] = num
		i += 1

	return size

'''
	Time Complexity: O(n)
	Space Complexity: O(n)

'''



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

size = remove_duplicates(arr)
print('\nThe array after removing the duplicates is', arr[:size])

