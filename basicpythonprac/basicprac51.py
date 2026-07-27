#Python Program to Find the GCD of Two Numbers
import math


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum =  math.gcd(a, b)
print("The GCD of", a, "and", b, "is", sum)