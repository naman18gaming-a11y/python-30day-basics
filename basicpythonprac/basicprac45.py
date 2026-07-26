#Python Program to Form an Integer that has Number of Digits at 10’s Place & LSD at 1’s Place
num = int(input("enter the number:"))
first = len(str(num))
sec = num % 10
res = first * 10 + sec

print('ans',res)