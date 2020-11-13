"""
Take an hour from the user as input and tell it is time for which meal.

• The user will input the number in a 24-hour format. So, 14 means 2 pm, 3 means 3 am, 18 means 6 pm, etc.\
• Valid inputs are 0 to 23. Inputs less than 0 or more than 23 are invalid in 24-hour clock.\
• Assume, Input will be whole numbers. For example, 3.5 will NOT be given as input.
Inputs: Message to be printed\ 4 to 6: Breakfast\ 12 to 13: Lunch\ 16 to 17: Snacks\ 19 to 20: Dinner\
For all other valid inputs, say "Patience is a virtue"\
For all other invalid inputs, say "Wrong time"
"""

n = int(input("Please enter hour"))
if (n > 23 or n < 0):
    print("Wrong time")
elif (n >= 4 and n <= 6):
    print("Breakfast time")
elif (n >= 12 and n <= 13):
    print("Lunch time")
elif (n >= 1 and n <= 17):
    print("Snacks time")
elif (n >= 19 and n <= 20):
    print("Dinner time")
else:
    print("Patience is virtue")
