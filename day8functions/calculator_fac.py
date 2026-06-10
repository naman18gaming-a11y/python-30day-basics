# Calculator Using Functions
def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
        print("The sum of the two numbers is:", result)
        return result
    elif operator == "-":
        result = num1 - num2
        print("The difference of the two numbers is:", result)
        return result
    elif operator == "*":
        result = num1 * num2
        print("The product of the two numbers is:", result)
        return result
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print("The quotient of the two numbers is:", result)
            return result
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Invalid operator. Please enter +, -, *, or /.")
        return None


print(calculator(10, 5, "+"))
