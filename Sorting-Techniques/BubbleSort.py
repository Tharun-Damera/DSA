'''
	Bubble Sort Algorithm
	Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

'''

def bubble_sort(arr):

	n = len(arr)
	swap_occurred = False

	for i in range(n-1, 0, -1):

		for j in range(i):

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swap_occurred = True

		if swap_occurred == False:
			break



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

print('\nBefore using Bubble Sort:', arr)
bubble_sort(arr)
print('After using Bubble Sort:', arr)


'''
	Time Complexity: O(n^2) -> Average & Worst Cases, 
					 O(n) -> Best Case (if input array is already sorted)

	Space Complexity: O(1)

'''