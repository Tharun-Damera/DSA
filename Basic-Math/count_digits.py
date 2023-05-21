"""
	Count digits in a number
	Problem Statement: Given an integer N , write program to count number of digits in N.

"""

def count_digits(num):
	n = num
	cnt = 0
	while n != 0:
		n = n // 10
		cnt += 1

	return cnt


num = int(input("Enter a number: "))
print('Number of digits:', count_digits(num))


'''
    Time complexity : O(log10(n))
    Space complexity : O(1)
'''

