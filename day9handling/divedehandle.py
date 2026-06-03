# Divide two numbers and handle zero
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("The result of the division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example calls
divide_numbers(10, 2)   # valid division
divide_numbers(5, 0)    # division by zero
