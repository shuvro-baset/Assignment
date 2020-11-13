"""
Write Python code of a program that reads two numbers from the user.
Your program should then print “First is greater” if the first number is greater,
“Second is greater” if the second number is greater, and “The numbers are equal” otherwise."""

var_1 = input("Please enter your first number")
var_2 = input("Please enter your second number")
print(type(var_1))
print(type(var_2))
var_3 = int(var_1)
var_4 = int(var_2)
if (var_3 > var_4):
    print("First is greater")
elif (var_4 > var_3):
    print("Second is greater")
else:
    print("The numbers are equal")
