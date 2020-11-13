"""
Write Python code of a program that finds the number of hours, minutes, and seconds in a given number of seconds.
"""

sec = int(input("Please enter amount of seconds"))
hour = sec / 3600
sec = sec % 3600
min = sec / 60
sec = sec % 60
print(int(hour), "hours", int(min), "minutes", sec, "seconds")
