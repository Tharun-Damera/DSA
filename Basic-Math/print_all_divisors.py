'''
    Print all Divisors of a given Number
    Problem Statement: Given a number, print all the divisors of the number. A divisor is a number that gives remainder as zero when divided.

'''

from math import sqrt

def print_divisors(num):
    print(f'The divisors of {num} are : ')
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:      
            print(i, end=' ')
            if i != num // i:
                print(num // i, end=' ')
            

num = int(input('Enter a number: '))
if num >= 1:
    print_divisors(num)
else:
    print(f'The number {num} has no divisors.')


'''
    Time complexity : O(√n)
    Space complexity : O(1)
'''