'''
	Count frequency of each element in the array
	Problem statement: Given an array, we have found the number of occurrences of each element in the array.

'''

# 1. Naive Approach
def frequency_count(arr):
	n = len(arr)
	visited = [False] * n

	print("\nNumber -> Frequency")
	for i in range(n):
		cnt = 0
		if visited[i] == True:
			continue

		for j in range(i, n):
			if arr[i] == arr[j]:
				visited[j] = True
				cnt += 1

		print(arr[i], ' -> ', cnt)


'''
	Time Complexity: O(n^2)
	Space Complexity: O(n) -> space for the visited array

'''



# 2. Optimal Approach
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
# frequency_count(arr)
count_frequency(arr)


'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> to store number and its occurence in dictionary

'''