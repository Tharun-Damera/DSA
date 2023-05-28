'''
	Insertion Sort Algorithm
	Problem Statement: Given an array of N integers, write a program to implement the Insertion sorting algorithm.

'''

def insertion_sort(arr):
	n = len(arr)

	for i in range(n):
		
		j = i
		while (j>0 and arr[j-1] > arr[j]):
			arr[j], arr[j-1] = arr[j-1], arr[j]
			j -= 1



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

print('\nBefore using Insertion Sort:', arr)
insertion_sort(arr)
print('After using Insertion Sort:', arr)


'''
	Time Complexity: O(n^2) -> Average & Worst Cases, 
					 O(n) -> Best Case (if input array is already sorted)

	Space Complexity: O(1)

'''