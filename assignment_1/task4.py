"""
Write Python code of a program that reads two numbers,
subtracts the smaller number from the larger one, and prints the result.
"""

var_1= input("Please enter your first number")
var_2= input("Please enter your second number")
print(type(var_1))
print(type(var_2))
var_3= int(var_1)
var_4= int(var_2)
if(var_3>var_4):
    print(var_3-var_4)
else:
    print(var_4-var_3)