'''
	Check if a number is Armstrong Number or not
	Problem Statement: Given a number, check if it is Armstrong Number or Not

'''

def is_armstrong(num):
    power = len(str(num))
    temp = num
    ans = 0
    while temp > 0:
        digit = temp % 10
        ans += digit ** power
        temp = temp // 10
    
    return num == ans
    

num = int(input('Enter a number: '))
ans = is_armstrong(num)    
if ans == True:
    print('It is an armstrong number')
else:
    print('It is not an armstrong number') 


'''
    Time complexity : O(log10(n))
    Space complexity : O(1)
'''

