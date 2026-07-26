#Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
import math
n = int(input("Enter the number of terms: "))
sum1 = 0
for i in range(1,1+n):
    sum1 = sum1 + 1/math.factorial(i)
    print(round(sum1,2))