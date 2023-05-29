'''
	Check if an Array is Sorted
	Problem Statement: Given an array of size n, write a program to check if the given array is sorted in 
	(ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

'''

def is_sorted(arr):

	n = len(arr)

	for i in range(n-1):
		if arr[i] > arr[i+1]:
			return False

	return True



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

if (is_sorted(arr)):
	print('The array is sorted.')
else:
	print('The array is not sorted.')



'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''