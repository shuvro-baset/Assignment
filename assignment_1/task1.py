"""
Write Python code of a program that reads two numbers from the user, and prints their sum, product, and difference.
"""

### Take input of 2 numbers from the user
var_1 = input('Please Enter Your First Number')
var_2 = input('Please Enter Your Second Number')

#Since input() function converts everything to String,
#for performing any kind of mathematical operation you need to convert them to int.
#For this conversion, we need to use int() function


# First, let's clarify whether the inputs are actually Strings or not.
print(type(var_1))
print(type(var_2))


# Convert Strings to integer using the int() function
var_3 = int(var_1)
var_4 = int(var_2)

# Perform Addition
sum = var_3 + var_4

# Perform Multiplication
product = var_3 * var_4

# Perform Substraction
difference = var_4 - var_3

# Print all the calculated results
print("Sum is", sum)
print("Product is", product)
print("Difference is", difference)