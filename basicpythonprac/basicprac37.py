#Python Program to Find All Pythagorean Triplets in the Range
import math


m = 3
n = 5

def pyt(m, n):
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2   
    return a, b, c

# call the function
triplet = pyt(m, n)
print("Pythagorean triplet:", triplet)
