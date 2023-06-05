'''
	Two Sum : Check if a pair with given sum exists in Array

'''

# 1. Brute Force 

def two_sum(arr, summ):

	n = len(arr)

	for i in range(n):
		for j in range(i+1, n):

			if arr[i] + arr[j] == summ:
				return i, j

	return -1, -1

'''
	Time Complexity: O(n^2) 
	Space Complexity: O(1)

'''


# 2. Better Approach	 --> [ Sorting & Two Pointers ]

def two_sum(arr, summ):

	arr.sort()
	left, right = 0, len(arr)-1

	while left < right:
		addn = arr[left] + arr[right]

		if addn == summ:
			return left, right

		elif addn < summ:
			left += 1

		else:
			right -= 1

	return -1, -1

'''
	Time Complexity: O(nlogn) 
	Space Complexity: O(1)		-> drawback is that the array gets modified (sorted)

'''


# 3. Optimal Approach  		----> [ Hashing / Dictionary ]

def two_sum(arr, summ):

	n = len(arr)
	lookup = {}

	for i in range(n):

		if summ - arr[i] in lookup:
			findex = lookup[summ-arr[i]]
			return findex, i

		lookup[arr[i]] = i

	return -1, -1

'''
	Time Complexity: O(n) 
	Space Complexity: O(n) 	-> extra space for the dictionary

'''


arr = [int(i) for i in input('\nEnter array elements (space separated): ').split()]
summ = int(input('Enter the sum value: '))

e1, e2 = two_sum(arr, summ)

print('\narr:', arr)
print(f'arr[{e1}] + arr[{e2}] = {summ}')
