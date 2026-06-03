# Print custom message when an exception occurs

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("The result of the division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Function calls outside
divide_numbers(10, 2)   # valid division
divide_numbers(5, 0)    # division by zero
