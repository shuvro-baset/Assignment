"""
Write Python code of a program that reads an integer, and prints the integer if it is a multiple of either 2 or 5.
"""

a = int(input("Please enter a number"))
if (a % 2 == 0 or a % 5 == 0):
    print(a)
