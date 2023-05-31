'''
	Count Maximum Consecutive One’s in the array
	Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

'''

def count_consecutive_1s(arr):

	cnt = max_cnt = 0

	for num in arr:

		if num == 1:
			cnt += 1
			max_cnt = cnt if max_cnt < cnt else max_cnt

		else:
			cnt = 0

	return max_cnt


'''
	Time Complexity: O(n) 
	Space Complexity: O(1)

'''


arr = [int(i) for i in input('\nEnter array elements of A (space separated): ').split()]

cnt = count_consecutive_1s(arr)

print(f'\nThe number of consecutive 1s in array:{arr} is {cnt}.')

