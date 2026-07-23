#check wheater the number is a strong number:
import math

num = int(input("Enter a number: "))
digits = str(num)

total = 0
for d in digits:
    total += math.factorial(int(d))

if total == num:
    print(num, "is a Strong number")
else:
    print(num, "is NOT a Strong number")
