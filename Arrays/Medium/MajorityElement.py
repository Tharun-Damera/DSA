'''
	Find the Majority Element that occurs more than N/2 times

	Problem Statement: Given an array of N integers, write a program to return an element that occurs 
	more than N/2 times in the given array. You may consider that such an element always exists in the array.

'''

# 1. Brute Force Approach

def majority_element(arr):

	n = len(arr)

	for i in range(n):
		cnt = 1
		for j in range(i+1, n):
			if arr[i] == arr[j]:
				cnt += 1

		if cnt > (n // 2):
			return arr[i]

	return -1

'''
	Time Complexity: O(n^2) 
	Space Complexity: O(1) 	

'''



arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

major = majority_element(arr)

print(f'The majority element in arr:{arr} is {major}')