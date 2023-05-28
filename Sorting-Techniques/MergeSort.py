'''
	Merge Sort Algorithm
	Problem:  Given an array of size n, sort the array using Merge Sort.

'''

def merge(arr, low, mid, high):

	i, j = low, mid+1
	temp = []

	while i <= mid and j <= high:
		if arr[i] <= arr[j]:
			temp.append(arr[i])
			i += 1
		else:
			temp.append(arr[j])
			j += 1

	while i <= mid:
		temp.append(arr[i])
		i += 1

	while j <= high:
		temp.append(arr[j])
		j += 1

	for i in range(low, high+1):
		arr[i] = temp[i-low]


def merge_sort(arr, low, high):

	if low >= high:
		return 

	mid = (low + high) // 2

	merge_sort(arr, low, mid)
	merge_sort(arr, mid+1, high)
	merge(arr, low, mid, high)



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

print('\nBefore using Merge Sort:', arr)
merge_sort(arr, 0, len(arr)-1)
print('After using Merge Sort:', arr)


'''
	Time Complexity: O(nlogn) -> Best, Average & Worst Cases,
	Space Complexity: O(1)

'''