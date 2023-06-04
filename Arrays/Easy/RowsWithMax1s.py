'''
	Row with max 1s
	Given a boolean 2D array of n x m dimensions where each row is sorted. 
	Find the 0-based index of the first row that has the maximum number of 1's.

'''

def rowWithMax1s(arr, m, n):

	i, j = 0, n-1

	row = -1

	while i < m and j >= 0:

		if arr[i][j] == 1:
			row = i
			j -= 1

		else:
			i += 1

	return row 

'''
	Time Complexity: O(m+n) 
	Space Complexity: O(1)

'''


rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of cols: '))

print('\nEnter array elements: ')
arr = [[int(input()) for _ in range(cols)] for _ in range(rows)]

row = rowWithMax1s(arr, rows, cols)

print(f'{row} row has maximum number of 1s.')

