"""
Write Python code of a program to compute and display a person’s weekly salary as determined by the following conditions:
If the hours worked are less than or equal to 40, the person receives Tk200.00 per hour,
else the person receives Tk8000.00 plus Tk300.00 for each hour worked over 40 hours.
The program should request the hours worked as input and should display the salary as output.
"""

a = int(input("Please enter hours worked"))
if (a <= 40):
    print("Tk200.00")
else:
    print(8000 + 300)
