"""
Write Python code of a program that reads an integer,
and prints the integer it is a multiple of either 2 or 5 but not both.

"""
a = int(input("Please enter a number"))
if (a % 10 != 0 and (a % 2 == 0 or a % 5 == 0)):
    print(a)
