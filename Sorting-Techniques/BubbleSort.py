'''
	Bubble Sort Algorithm
	Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

'''

def bubble_sort(arr):

	n = len(arr)

	for i in range(n-1, 0, -1):

		for j in range(i):

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

bubble_sort(arr)
print('After Sorting using Bubble Sort the array is', arr)


'''
	Time Complexity: O(n^2)
	Space Complexity: O(1)

'''