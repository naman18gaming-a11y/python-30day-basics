# Take user input and convert it to integer using try-except.
try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")