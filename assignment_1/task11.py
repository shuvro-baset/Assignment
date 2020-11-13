"""
Write Python code of a program that reads a student’s mark for a single subject,
and prints out the corresponding grade for that mark.
The mark ranges and corresponding grades are shown in the table below.
You need to make sure that the marks are valid. For example, a student cannot receive -5 or 110.
So the valid marks range is 0 to 100.
"""

a=int(input("Please enter the marks"))
if(a>=90 and a<=100):
    print("A")
elif(a>=80 and a<=89):
    print("B")
elif(a>=70 and a<=79):
    print("C")
elif(a>=60 and a<=69):
    print("D")
elif(a>=50 and a<=59):
    print("E")
else:
    print("F")