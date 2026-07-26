#Python Program to Test Collatz Conjecture for a Given Number
num = int(input("enter a value:"))
if num % 2 == 0 :
    print("ans",num/2)
else:
    print("ans",3*num+1)