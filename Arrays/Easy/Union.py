'''
	Union of Two Sorted Arrays
	Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

	The union of two arrays can be defined as the common and distinct elements in the two arrays.
	NOTE: Elements in the union should be in ascending order.

'''

# 1. Brute Force
def union_of_two_arrays(A, B):

	union = set()

	for num in A:
		union.add(num)

	for num in B:
		union.add(num)

	return list(union)

'''
	Time Complexity: O(m+n)  	[m -> len(A), n -> len(B)]
	Space Complexity: O(m+n)

'''


A = [int(i) for i in input('\nEnter array elements of A (space separated): ').split()]
B = [int(i) for i in input('\nEnter array elements of B (space separated): ').split()]
union = union_of_two_arrays(A, B)

print(f'\n A:{A} \n B:{B} \n\n AUB:{union}.')
