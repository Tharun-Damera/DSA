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






num = int(input("Enter n value: "))

pattern7(num)
