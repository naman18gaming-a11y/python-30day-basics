#Python Program to Find the Roots of a Quadratic Equation
import math
a = 1
b = -5
c = 2

# to find the discriminat i willl use the formula
D = b**2 - 4*a*c
print(D)
# now to find the sqaure root we will use this formual:
root = (-b + math.sqrt(D))/(2*a)
print(root)