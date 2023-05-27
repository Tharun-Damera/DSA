'''
	Find the highest/lowest frequency element

'''
import sys

def frequent_elements(arr):

	freq = {}
	max_value = ~sys.maxsize
	min_value = sys.maxsize

	for num in arr:
		freq[num] = freq.get(num, 0) + 1

	for key, value in freq.items():
		if value > max_value:
			max_value = value
			highest = key

		if value < min_value:
			min_value = value
			lowest = key

	print('Element with highest freqency is', highest)
	print('Element with lowest freqency is', lowest)



arr = [int(i) for i in input('Enter the array elements (space separated): ').split()]
frequent_elements(arr)


'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> space required for dictionary

'''