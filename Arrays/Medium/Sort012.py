'''
	Sort an array of 0s, 1s and 2s

	Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
	Write a program to in-place sort the array without using inbuilt sort functions.

'''

# 1. Brute Force

# def sort_arr(arr):

# 	arr.sort()
# 	return

'''
	Time Complexity: O(nlogn) 
	Space Complexity: O(1) 

'''



# 2. Better Approach	--> [ Count 0s, 1s & 2s ]

def sort_arr(arr):

	n = len(arr)
	cnt_0 = cnt_1 = cnt_2 = 0

	for num in arr:

		if num == 0:
			cnt_0 += 1

		elif num == 1:
			cnt_1 += 1

		else:
			cnt_2 += 1


	for i in range(n):
		if i < cnt_0:
			arr[i] = 0

		elif i < cnt_0 + cnt_1:
			arr[i] = 1

		else:
			arr[i] = 2


'''
	Time Complexity: O(n) 
	Space Complexity: O(1) 

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]

print('\nBefore Sorting arr: ', arr)

sort_arr(arr)

print('After Sorting  arr: ', arr)
