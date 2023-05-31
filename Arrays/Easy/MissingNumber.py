'''
	Find the missing number in an array
	Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
	Find the number(between 1 to N), that is not present in the given array.

'''

# 1. Brute Force

def find_missing_num(arr, n):

	for i in range(1, n+1):
		flag = 0

		for num in arr:    # Linear search
			if num == i:
				# element found 
				flag = 1
				break

		if flag == 0:
			# element not found -> missing num
			return i

	return -1

'''
	Time Complexity: O(n^2) 
	Space Complexity: O(1)

'''

# 2. Better Approach  			--> [Hashing -> Hash array]

def find_missing_num(arr, n):

	hash_arr = [0] * (n+1)

	for num in arr:
		hash_arr[num] += 1

	for i in range(1, n+2):
		if hash_arr[i] == 0:
			return i

	return -1


'''
	Time Complexity: O(n) 
	Space Complexity: O(n)

'''


##  Optimal Approaches
#		|
#		--> Summation (Sum of n natural numbers formula) method
# 		|
#		--> XOR method *


# 3. Summation Method 

def find_missing_num(arr, n):

	n_sum = n * (n+1) // 2

	arr_sum = 0

	for num in arr:
		arr_sum += num

	missing_num = n_sum - arr_sum

	return missing_num


'''
	Time Complexity: O(n) 
	Space Complexity: O(1)

'''


# 4. XOR Method

def find_missing_num(arr, n):

	xor_n = xor_arr = 0

	for num in range(1, n+1):
		xor_n = xor_n ^ num

	for num in arr:
		xor_arr = xor_arr ^ num

	missing_num = xor_n ^ xor_arr

	return missing_num



'''
	Time Complexity: O(n) 
	Space Complexity: O(1)

'''



arr = [int(i) for i in input('\nEnter array elements of A (space separated): ').split()]
n = int(input('Enter n value: '))

missing_num = find_missing_num(arr, n)

print(f'The missing number in array: {arr} is {missing_num}.')
