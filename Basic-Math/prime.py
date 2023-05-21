'''
	Check if a number is prime or not
	Problem Statement: Given a number, check whether it is prime or not. A prime number is a natural number that is only divisible by 1 and by itself.

'''

from math import sqrt

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    
    return True

num = int(input('Enter a number: '))
if is_prime(num):
	print('It is a prime number.')
else:
	print('It is not a prime number.')
