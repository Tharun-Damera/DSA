'''
	Find the number that appears once, and the other numbers twice
	Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

'''

# 1. Brute Force

def get_single_element(arr):

	n = len(arr)

	for i in range(n):
		cnt = 1
		for j in range(i+1, n):
			if arr[i] == arr[j]:
				cnt += 1

		if cnt == 1:
			return arr[i]

	return -1

'''
	Time Complexity: O(n^2) 
	Space Complexity: O(1)

'''


arr = [int(i) for i in input('\nEnter array elements of A (space separated): ').split()]

element = get_single_element(arr)

print(f'\nThe element which occurs only once in the array:{arr} is {element}.')
