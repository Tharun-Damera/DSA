'''
	Remove Duplicates in-place from sorted array

'''

# 1. Brute Force
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


# 2. Optimal Approach
def remove_duplicates(arr):
	n = len(arr)

	if n <= 1:
		return 

	t1, t2 = 0, 1

	while t2 < n:
		if arr[t1] == arr[t2]:
			t2 += 1
		else:
			t1 += 1
			arr[t1] = arr[t2]
			t2 += 1

	return t1

'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

size = remove_duplicates(arr)
print('\nThe array after removing the duplicates is', arr[:size])

