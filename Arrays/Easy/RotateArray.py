'''
	Rotate array by K elements
	Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

'''

# 1. Brute Force
def rotate_array(arr, direction, k):

	n = len(arr)
	k = k % n
	tmp = [0] * k

	if direction == 'l':

		for i in range(k):
			tmp[i] = arr[i]

		for i in range(k, n):
			arr[i-k] = arr[i]

		j = 0
		for i in range(n-k, n):
			arr[i] = tmp[j]
			j += 1


	elif direction == 'r':
		
		j = 0
		for i in range(n-k, n):
			tmp[j] = arr[i]
			j += 1

		for i in range(n-k):
			arr[i+k] = arr[i]
		
		for i in range(k):
			arr[i] = tmp[i]

'''
	Time Complexity: O(n)
	Space Complexity: O(k)

'''



# 2. Optimal Approach -> *[ REVERSAL ALGORITHM ]

def reverse_array(arr, left, right):

	while left < right:
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1

def rotate_array(arr, direction, k):

	n = len(arr)
	k = k % n

	if direction == 'l':
		reverse_array(arr, 0, k-1)
		reverse_array(arr, k, n-1)

	elif direction == 'r':
		reverse_array(arr, n-k, n-1)
		reverse_array(arr, 0, n-k-1)

	reverse_array(arr, 0, n-1)

'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]
direction = input('Enter the direction in which array has to be rotated (l -> left/r -> right): ').lower()
k = int(input('Enter the k value: '))

rotate_array(arr, direction, k)

print(f"\nThe array after rotating it in {'left' if direction == 'l' else 'right'} by {k} elements is {arr}.")

