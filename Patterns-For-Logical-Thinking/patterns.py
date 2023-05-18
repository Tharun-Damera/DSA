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






num = int(input("Enter n value: "))

pattern1(num)
