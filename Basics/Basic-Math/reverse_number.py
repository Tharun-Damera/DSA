'''
    Reverse a number in C.

    Problem Statement: Given a number N reverse the number and print it.

'''

def reverse_num(num):
    temp = num
    rev = 0 
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    
    return rev


n = int(input('Enter a number: '))
print(f'The reverse of the number {n} is {reverse_num(n)}.')



'''
    Time complexity : O(log10(n))
    Space complexity : O(1)
'''

