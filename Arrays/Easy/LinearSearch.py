'''
	Linear Search
	Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. 
	If present print the index of the element or print -1.

'''

def linear_search(arr, element):

	n = len(arr)

	for i in range(n):
		if arr[i] == element:
			return i

	return -1



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]
element = int(input('Enter the element to search in the array: '))

index = linear_search(arr, element)

if index != -1:
	print(f'\nThe element {element} is present at {index}th index in the array {arr}.')
else:
	print(f'\nThe element {element} is not present in the array {arr}.')



'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''