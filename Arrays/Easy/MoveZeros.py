'''
	Move all Zeros to the end of the array
	Problem Statement: You are given an array of integers, your task is to move all the zeros in the array 
	to the end of the array and move non-negative integers to the front by maintaining their order.

'''

# 1. Brute Force
def move_zeros(arr):

	n = len(arr)
	tmp = []
	cnt = 0

	for num in arr:
		if num != 0:
			tmp.append(num)
		else:
			cnt += 1

	while cnt:
		tmp.append(0)
		cnt -= 1

	return tmp

'''
	Time Complexity: O(n)
	Space Complexity: O(n)

'''

# 2. Optimal Approach

def move_zeros(arr):

	n = len(arr)
	t1, t2 = -1, 0

	while t2 < n:
		if arr[t2] == 0:
			t2 += 1
		else:
			t1 += 1
			arr[t1], arr[t2] = arr[t2], arr[t1]
			t2 += 1

'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]
move_zeros(arr)

print('\nAfter moving the zeros to the end the array is', arr)

