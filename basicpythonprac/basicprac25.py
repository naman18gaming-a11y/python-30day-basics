# Python Program to Find Whether a Number is a Power of Two

def power_of_two(n):
    if n < 0:
        print("Negative numbers are not powers of two")
    elif n > 0:
        print(n * n)


power_of_two(4)