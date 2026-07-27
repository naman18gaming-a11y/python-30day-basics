# Python Program to Find the LCM of Two Numbers
import math
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
sum = a*b / math.gcd(a, b)
print("The LCM of", a, "and", b, "is", sum)
