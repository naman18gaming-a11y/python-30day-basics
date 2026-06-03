# Factorial of a number using function
def factorial(num):
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    elif num == 0 or num == 1:
        print("Factorial of", num, "is 1.")
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        print("Factorial of", num, "is", result)

num = 5
factorial(num)
