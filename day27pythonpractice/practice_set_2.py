#simple calculator 
print("--CALCULATOR--")
a = int(input("enetr the value of first number"))
b = int(input("enter the value of second number"))
choice  = int(input("choose between 1-4 "))

if choice == 1:
    print("the sum of two num is", a+b)
elif choice == 2:
    print("the diff of two number is", a-b)
elif choice == 3:
    print("the multiple of two number is", a*b)
else:
    print("invalid choice")