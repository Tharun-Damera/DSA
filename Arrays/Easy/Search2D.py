'''
	Search in a sorted 2D matrix

	Problem Statement: Given an m*n 2D matrix and an integer, write a program to find if the given integer exists in the matrix.

	Given matrix has the following properties:
	 - Integers in each row are sorted from left to right.
	 - The first integer of each row is greater than the last integer of the previous row

'''

# 1. Brute Force Approach

def search_2D(arr, key):

	m, n = len(arr), len(arr[0])

	for i in range(m):
		for j in range(n):

			if key == arr[i][j]:
				return True

	return False

'''
	Time Complexity: O(m*n) 
	Space Complexity: O(1)

'''


# 2. Good Approach   --> [Individual row - Binary search]

def binary_search(arr, key):

	low, high = 0, len(arr)-1

	while low <= high:
		mid = low + (high - low) // 2

		if key == arr[mid]:
			return True
		elif key < arr[mid]:
			high = mid - 1
		else:
			low = mid + 1

	return False


def search_2D(arr, key):

	m = len(arr)

	for i in range(m):

		if binary_search(arr[i], key) == True:
			return True

	return False


'''
	Time Complexity: O(m*log(n)) 
	Space Complexity: O(1)

'''


# 3. Better Approach   ---> [Similar to Binary Search (Left / Bottom)]

def search_2D(arr, key):

	m, n = len(arr), len(arr[0])

	i, j = 0, n - 1

	while i < m and j >= 0:

		if key == arr[i][j]:
			return True

		elif key < arr[i][j]:
			j -= 1 	# Left 

		else:
			i += 1  # Bottom

	return False


'''
	Time Complexity: O(log(m*n)) 
	Space Complexity: O(1)

'''


rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of cols: '))

print('\nEnter array elements: ')

arr = [[int(input()) for _ in range(cols)] for _ in range(rows)]

key = int(input('Enter search element: '))

is_present = search_2D(arr, key)

if is_present:
	print(f'Element {key} found.')
else:
	print(f'Element {key} not found.')
