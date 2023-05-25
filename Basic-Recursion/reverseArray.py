'''
	Reverse a given Array
	Problem Statement: You are given an array. The task is to reverse the array and print it. 

'''

# 1. Iterative Approach
def reverse_array(arr):
	
	left, right = 0, len(arr)-1

	while left < right:
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1

'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''


# 2. Recursive Approach
def reverse_array_II(arr, start, end):
	if start < end:
		arr[start], arr[end] = arr[end], arr[start]

		reverse_array_II(arr, start+1, end-1)

'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''



arr = [int(i) for i in input('Enter array elements (space separated): ').split()]

reverse_array(arr)
print('First Reversal using Iterative Method:', arr)

reverse_array_II(arr, 0, len(arr)-1)
print('Second Reversal using Recursive Method:', arr)
