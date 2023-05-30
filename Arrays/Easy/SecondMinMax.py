'''
	Find Second Smallest and Second Largest Element in an array
	Problem Statement: Given an array, find the second smallest and second largest element in the array. 
	Print ‘-1’ in the event that either of them doesn’t exist.

'''

import sys

def second_min_max(arr):

	if len(arr) < 4:
		return -1, -1

	first_max = sec_max = ~sys.maxsize
	first_min = sec_min = sys.maxsize


	for num in arr:

		if num > first_max:
			sec_max = first_max
			first_max = num

		elif num > sec_max and num != first_max:
			sec_max = num

		if num < first_min:
			sec_min = first_min
			first_min = num
			
		elif num < sec_min and num != first_min:
			sec_min = num


	return sec_min, sec_max


'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

sec_min, sec_max = second_min_max(arr)

print(f'\nSecond Min Value = {sec_min}')
print(f'Second Max Value = {sec_max}')

