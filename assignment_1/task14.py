"""
Suppose the following expressions are used to calculate the values of L for different values of S:

L=3000−125S2 if S<100
L=120004+S2/14900 if S≥100
Write a Python code of a program that reads a value of S and then calculates the value of L.
"""

S = int(input("Please enter value of S"))
L = 3000 - 125 * (S ** 2)
L1 = 12000 / (4 + (S ** 2) / 14900)
if (S < 100):
    print(L)
if (S >= 100):
    print(L1)
