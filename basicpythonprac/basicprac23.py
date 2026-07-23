#Python Program to Find the Prime Factors of a Number
n = int(input("enter the the number="))
i = 2
while n > 1:
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i += 1