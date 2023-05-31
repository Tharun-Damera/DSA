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

# 2. Optimal Approach     		--> [TWO POINTERS APPROACH] -> Applicable only when the arrays are sorted.

def union_of_two_arrays(A, B):
	m, n = len(A), len(B)
	union = []

	t1 = t2 = 0
	while t1 < m and t2 < n:

		if A[t1] == B[t2]:
			if len(union) == 0 or union[-1] != A[t1]:
				union.append(A[t1])
			t1 += 1
			t2 += 1

		elif A[t1] < B[t2]:
			if len(union) == 0 or union[-1] != A[t1]:
				union.append(A[t1])
			t1 += 1
		else:
			if len(union) == 0 or union[-1] != B[t2]:
				union.append(B[t2])
			t2 += 1

	while t1 < m:
		if len(union) == 0 or union[-1] != A[t1]:
			union.append(A[t1])
		t1 += 1

	while t2 < n:
		if len(union) == 0 or union[-1] != B[t2]:
			union.append(B[t2])
		t2 += 1


	return union

'''
	Time Complexity: O(m+n) 
	Space Complexity: O(1) -> if you don't consider the space for union array which is output

'''


A = [int(i) for i in input('\nEnter array elements of A (space separated): ').split()]
B = [int(i) for i in input('\nEnter array elements of B (space separated): ').split()]
union = union_of_two_arrays(A, B)

print(f'\n A:{A} \n B:{B} \n\n AUB:{union}.')
