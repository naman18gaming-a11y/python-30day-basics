#Python Program to Check If Two Numbers are Amicable Numbers or Not

num = int(input("Enter a number: "))

for i in range(1, num+1):
    if num % i == 0:   
        print(i)
divisor_sum = 0
for i in range(1, num):
    if num % i == 0:
        divisor_sum += i

if divisor_sum == num:
    print("amicable")
else:
    print("not amicable")