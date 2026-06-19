#Python Program to Check Whether a given Year is a Leap Year
num = int(input("enter the number:  "))
if (num % 4==0  and num % 100 != 0 or num%400==0):
    print("leap")
else:
    print("no")