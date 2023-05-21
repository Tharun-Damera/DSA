'''
	Check if a number is Palindrome or Not

	Problem Statement:  Given a number check if it is a palindrome.

	- An integer is considered a palindrome when it reads the same backward as forward.
'''

def is_palindrome(num):
    temp = num
    rev = 0 
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    
    return num == rev


n = int(input('Enter a number: '))
ans = is_palindrome(n)
if ans == True:
    print('It is a palindrome.')
else:
    print('It is not a palindrome.')