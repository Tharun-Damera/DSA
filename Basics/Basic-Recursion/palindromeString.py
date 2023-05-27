'''
	Check if the given String is Palindrome or not
	Problem Statement: “Given a string, check if the string is palindrome or not.”  
	A string is said to be palindrome if the reverse of the string is the same as the string.
'''

# 1. Iterative Approach
def is_palindrome(string):

	start, end = 0, len(string)-1

	while start < end:
		if string[start] != string[end]:
			return False

		start += 1
		end -= 1

	return True

'''
	Time Complexity: O(n)
	Space Complexity: O(1)

'''

# 2. Recursive Approach
def is_palindrome_II(string, start, end):

	if start >= end:
		return True

	if string[start] != string[end]:
		return False		

	return is_palindrome_II(string, start+1, end-1)

'''
	Time Complexity: O(n)
	Space Complexity: O(n) -> due to recursion stack

'''


string = input("Enter a string: ")

ans = is_palindrome_II(string, 0, len(string)-1)

if ans:
    print('It is a palindrome.')
else:
    print('It is not a palindrome.')

