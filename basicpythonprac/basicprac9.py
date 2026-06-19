num = int(input("enter the number:  "))
total = 0
while (num > 0 ):
    dig = num % 10
    total = total + dig
    n = num // 10
    print(total)