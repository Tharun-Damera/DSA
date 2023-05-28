'''
	Quick Sort Algorithm
	Problem Statement:  Given an array of n integers, sort the array using the Quicksort method.
'''

def partition(arr, low, high):
	pivot = arr[low]
	i, j = low, high

	while i < j:
		while arr[i] <= pivot and i < high:
			i += 1
		while arr[j] > pivot and j > low:
			j -= 1

		if i < j:
			arr[i], arr[j] = arr[j], arr[i]

	arr[low], arr[j] = arr[j], arr[low]
	return j


def quick_sort(arr, low, high):

	if low >= high:
		return

	pivot_index = partition(arr, low, high)
	quick_sort(arr, low, pivot_index-1)
	quick_sort(arr, pivot_index+1, high)




arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

print('\nBefore using Quick Sort:', arr)
quick_sort(arr, 0, len(arr)-1)
print('After using Quick Sort:', arr)


'''
	Time Complexity: O(nlogn) -> Best & Average cases
					 O(n^2)   -> Worst Case (pivot is always largest or smallest element)
	Space Complexity: O(1)

'''