#Python Program to Check Whether a Given Number is Perfect Number
num = int(input("ENTER THE NUMBER: "))
for i in range (1,num-1):
    if num % i == 0:
                sum_of_divisors += i
    if sum_of_divisors == num:
            print("yesssss",num)
    else:
            print("neh",num)
