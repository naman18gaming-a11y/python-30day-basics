#  print max number in function
def max_num(num1, num2):
    if num1 > num2:
        print(num1, "is the max number.")
    else:
        print(num2, "is the max number.")
        return num2

print(max_num(10, 20))