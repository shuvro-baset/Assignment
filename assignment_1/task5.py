"""
Write Python code of a program that reads a number,
and prints “The number is even” or “The number is odd”, depending on whether the number is even or odd.
"""

var= input("Please enter your number")
print(type(var))
var_1= int(var)
if(var_1%2==0):
    print("The number is even")
else:
    print("The number is odd")