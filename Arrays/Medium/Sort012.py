'''
	Sort an array of 0s, 1s and 2s

	Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
	Write a program to in-place sort the array without using inbuilt sort functions.

'''

# 1. Brute Force

def sort_arr(arr):

	arr.sort()
	return

'''
	Time Complexity: O(nlogn) 
	Space Complexity: O(1) 

'''




arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

print('\nBefore Sorting arr: ', arr)

sort_arr(arr)

print('After Sorting arr: ', arr)
