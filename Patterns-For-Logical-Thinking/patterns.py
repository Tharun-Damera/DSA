"""
Pattern-1: Rectangular Star Pattern

Input: N = 6
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

"""
def pattern1(n):
	print("Pattern-1: ")
	for i in range(n):	
		for j in range(n):
			print('*', end=' ')
		print()


"""
Pattern-2: Right-Angled Triangle Pattern

Input Format: N = 6
Output:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *

"""
def pattern2(n):
	print("Pattern-2: ")
	for i in range(n):
		for j in range(i+1):
			print('*', end=' ')
		print()


"""
Pattern – 3: Right-Angled Number Pyramid

Input Format: N = 6
Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

"""
def pattern3(n):
	print("Pattern-3: ")
	for i in range(1, n+1):
		for j in range(1, i+1):
			print(j, end=' ')
		print()


"""
Pattern – 4: Right-Angled Number Pyramid – II

Input Format: N = 6
Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

"""
def pattern4(n):
	print("Pattern-4: ")
	for i in range(1, n+1):
		for j in range(1, i+1):
			print(i, end=' ')
		print()


"""
Pattern-5: Inverted Right Pyramid

Input Format: N = 6
Output:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

"""
def pattern5(n):
	print("Pattern-5: ")
	for i in range(n):
		for j in range(n-i):
			print('*', end=' ')
		print()


"""
Pattern – 6: Inverted Numbered Right Pyramid

Input Format: N = 6
Output:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

"""
def pattern6(n):
	print("Pattern-6: ")
	for i in range(n):
		for j in range(1, n-i+1):
			print(j, end=' ')
		print()


"""
Pattern – 7: Star Pyramid

Input Format: N = 6
Output:
     *     
    ***    
   *****   
  *******  
 ********* 
***********

"""
def pattern7(n):
	print("Pattern-7: ")
	for i in range(n):
		for j in range(n-i-1):
			print(' ', end='')
		for j in range(2*i+1):
			print('*', end='')
		for j in range(n-i-1):
			print(' ', end='')

		print()


"""
Pattern – 8: Inverted Star Pyramid

Input Format: N = 6
Output:
***********
 *********
  *******
   ***** 
    ***    
     *

"""
def pattern8(n):
	print("Pattern-8: ")
	for i in range(n):
		for j in range(i):
			print(' ', end='')
		for j in range(2*n - (2*i+1)):
			print('*', end='')
		for j in range(i):
			print(' ', end='')
		print()


"""
Pattern – 9: Diamond Star Pattern

Input Format: N = 6
Output:
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *

"""
def pattern9(n):
	print("Pattern-9: ")
	for i in range(n):
		for j in range(n-i-1):
			print(' ', end='')
		for j in range(2*i+1):
			print('*', end='')
		for j in range(n-i-1):
			print(' ', end='')

		print()
	for i in range(n):
		for j in range(i):
			print(' ', end='')
		for j in range(2*n - (2*i+1)):
			print('*', end='')
		for j in range(i):
			print(' ', end='')
		print()


"""
Pattern – 10: Half Diamond Star Pattern

Input Format: N = 6
Output:
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *

"""
def pattern10(n):
	print("Pattern-10: ")
	for i in range(1, 2*n):
		stars = i if i <= n else 2*n-i

		for j in range(stars):
			print('*', end='')
		print()

"""
Pattern – 11: Binary Number Triangle Pattern

Input Format: N = 6
Output:
1
01
101
0101
10101
010101

"""
def pattern11(n):
	print("Pattern-11: ")
	for i in range(n):
		for j in range(i+1):
			if (i+j) % 2 == 0:
				print('1', end='')
			else:
				print('0', end='')
		print()



"""
Pattern – 12: Number Crown Pattern

Input Format: N = 6
Output:
1          1
12        21
12       321
1234    4321
12345  54321
123456654321

"""
def pattern12(n):
	print("Pattern-12: ")
	for i in range(1, n+1):
	    for j in range(1, i+1):
	        print(j, end="")
	    for j in range(2*(n-i)):
	        print(" ", end="")
	    for j in range(i, 0, -1):
	        print(j, end="")
	     
	    print()



"""
Pattern – 13: Increasing Number Triangle Pattern

Input Format: N = 6
Output:
1
2  3
4  5  6
7  8  9  10
11  12  13  14  15
16  17  18  19  20  21

"""
def pattern13(n):
	val = 1
	print("Pattern-13: ")
	for i in range(n):
	    for j in range(i+1):
	        print(val, end=" ")
	        val += 1
	    print()

"""
Pattern – 14: Increasing Letter Triangle Pattern

Input Format: N = 6
Output:
A
A B
A B C
A B C D
A B C D E
A B C D E F

"""
def pattern14(n):
	val = 65
	print("Pattern-14: ")
	for i in range(n):
		for j in range(i+1):
			ch = chr(val+j)
			print(ch, end=" ")
		print()



"""
Pattern – 15: Reverse Letter Triangle Pattern

Input Format: N = 6
Output:
A B C D E F
A B C D E 
A B C D
A B C
A B
A

"""

def pattern15(n):
	val = 65
	print("Pattern-15: ")
	for i in range(n):
		for j in range(n-i):
			ch = chr(val+j)
			print(ch, end=" ")
		print()


"""
Pattern – 16: Alpha-Ramp Pattern

Input Format: N = 6
Output:
A 
B B
C C C
D D D D
E E E E E
F F F F F F

"""
def pattern16(n):
	val = 65
	print("Pattern-16: ")
	for i in range(n):
		for j in range(i+1):
			ch = chr(val+i)
			print(ch, end=" ")
		print()

"""
Pattern – 17: Alpha-Hill Pattern

Input Format: N = 6
Output:
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA

"""
def pattern17(n):
	print("Pattern-17: ")
	for i in range(n):
		for j in range(n-i-1):
			print(' ', end='')
		val = 64
		for j in range(2*i+1):
			if j <= (2*i+1)/2:
				val += 1
				ch = chr(val)
			else:
				val -= 1
				ch = chr(val)
			print(ch, end='')
		print()


"""
Pattern – 18: Alpha-Triangle Pattern

Input Format: N = 6
Output:
F
E F
D E F
C D E F
B C D E F
A B C D E F

"""
def pattern18(n):
	print("Pattern-18: ")
	for i in range(n):
		val = 65+n-1-i
		for j in range(val, val+i+1):
			ch = chr(j)
			print(ch, end=' ')
		print()

"""
Pattern – 19: Symmetric-Void Pattern

Input Format: N = 6
Output:
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************

"""
def pattern19(n):
	print("Pattern-19: ")
	for i in range(n, 0, -1):
		for j in range(1, i+1):
			print('*', end='')
		for j in range(2*(n-i)):
			print(' ', end='')
		for j in range(1, i+1):
			print('*', end='')
		print()
	for i in range(1, n+1):
		for j in range(1, i+1):
			print('*', end='')
		for j in range(2*(n-i)):
			print(' ', end='')
		for j in range(1, i+1):
			print('*', end='')
		print()

"""
Pattern – 20: Symmetric-Butterfly Pattern

Input Format: N = 6
Output:
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

"""
def pattern20(n):
	print("Pattern-20: ")
	for i in range(1, n+1):
		for j in range(1, i+1):
			print('*', end='')
		for j in range(2*(n-i)):
			print(' ', end='')
		for j in range(1, i+1):
			print('*', end='')
		print()
	for i in range(n-1, 0, -1):
		for j in range(1, i+1):
			print('*', end='')
		for j in range(2*(n-i)):
			print(' ', end='')
		for j in range(1, i+1):
			print('*', end='')
		print()

"""
Pattern – 21: Hollow Rectangle Pattern

Input Format: N = 6
Output:
******
*    *
*    *
*    *
*    *
******

"""
def pattern21(n):
	print("Pattern-21: ")
	for i in range(n):
		for j in range(n):
			if i == 0 or j == 0 or i == n-1 or j == n-1:
				print('*', end='')
			else:
				print(' ', end='')
		print()



"""
Pattern – 22: The Number Pattern

Input Format: N = 6
Output:
6 6 6 6 6 6 6 6 6 6 6 
6 5 5 5 5 5 5 5 5 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 2 1 2 3 4 5 6 
6 5 4 3 2 2 2 3 4 5 6 
6 5 4 3 3 3 3 3 4 5 6 
6 5 4 4 4 4 4 4 4 5 6 
6 5 5 5 5 5 5 5 5 5 6 
6 6 6 6 6 6 6 6 6 6 6

"""
def pattern22(n):
	print("Pattern-22: ")
	for i in range(1-n, n):
		for j in range(1-n, n):
			if abs(i) < abs(j):
				print(abs(j)+1, end=' ')
			else:
				print(abs(i)+1, end=' ')
		print()




num = int(input("Enter n value: "))


pattern22(num)
