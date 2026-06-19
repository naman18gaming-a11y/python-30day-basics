#Python Program to Find Sum of Digits of a Number
num = int(input("enter the number: "))
total_sum = 0
for numm in str(abs(num)):
    total_sum += int(numm)
    print("total sum",total_sum)