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






num = int(input("Enter n value: "))

pattern2(num)
