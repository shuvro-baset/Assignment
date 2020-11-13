"""
Write Python code of a program that reads an integer,
and prints the integer if it is NOT a multiple of 2 OR NOT a multiple of 5.

"""

a = int(input("Please enter a number"))
if (a % 2 != 0 or a % 5 != 0):
    print(a)
