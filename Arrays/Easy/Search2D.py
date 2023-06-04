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
	Time Complexity: O(n^2) 
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
