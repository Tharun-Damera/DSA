'''
	Selection Sort Algorithm
	Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

'''

def selection_sort(arr):

	n = len(arr)

	for i in range(n-1):
		min_index = i

		for j in range(i+1, n):

			if arr[j] < arr[min_index]:
				min_index = j

		arr[i], arr[min_index] = arr[min_index], arr[i]



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]
selection_sort(arr)
print('After Sorting using Selection Sort the array is', arr)


'''
	Time Complexity: O(n^2) -> Best, Average & Worst Case
	Space Complexity: O(1)

'''