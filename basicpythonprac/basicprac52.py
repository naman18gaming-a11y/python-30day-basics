#Python Program to Find the LCM of Two Numbers using Recursion
# Python Program to Find the LCM of Two Numbers using Recursion

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)   #

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))
