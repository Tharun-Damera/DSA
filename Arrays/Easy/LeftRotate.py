'''
	Left Rotate array by one place

'''

def rotate_left(arr):
	n = len(arr)
	if n <= 1:
		return

	element = arr[0]

	for i in range(1, n):
		arr[i-1] = arr[i]

	arr[-1] = element


'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

rotate_left(arr)

print('\nThe array after rotating it by one place is', arr)
