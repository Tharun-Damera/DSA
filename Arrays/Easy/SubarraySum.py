'''
	Longest Subarray with given Sum K
	Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

'''

# 1. Brute Force

def longest_subarray_length(arr, k):

	n = len(arr)
	max_len = 0

	for i in range(n):
		addn = 0
		for j in range(i, n):
			addn += arr[j]

			if addn == k:
				max_len = max(max_len, j-i+1)
			elif addn > k:
				break

	return max_len


'''
	Time Complexity: O(n^2) 
	Space Complexity: O(1)

'''

arr = [int(i) for i in input('\nEnter array elements of A (space separated): ').split()]
k = int(input('Enter sum k value: '))

length = longest_subarray_length(arr, k)

print(f'\nThe length of longest subarray of the array:{arr} is {length}.')
