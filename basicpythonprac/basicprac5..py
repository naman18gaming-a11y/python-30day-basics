#Python Program to Print All Integers that Aren’t Divisible by Either 2 or 3
for num in  range(0,51):
    if num % 2 and num % 3 != 0:
        print("num",num)
