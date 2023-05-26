'''
	Count frequency of each element in the array
	Problem statement: Given an array, we have found the number of occurrences of each element in the array.

'''

def count_frequency(arr):
	
	freq = {}

	for num in arr:
		if num not in freq:
			freq[num] = 1
		else:
			freq[num] += 1

	print("\nNumber -> Frequency")

	for k, v in freq.items():
		print(k, ' -> ', v)



arr = [int(i) for i in input('Enter the array elements (space separated): ').split()]
count_frequency(arr)

'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> to store number and its occurence in dictionary

'''