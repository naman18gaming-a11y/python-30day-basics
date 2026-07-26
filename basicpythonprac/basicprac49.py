# Sum of Sine Series
import math


n = int(input("Enter the number of terms: "))       
sum1 = 0
for i in range(1, n + 1):
    sum1 += ((-1) ** (i + 1)) * (1 / math.factorial(2 * i - 1))
print("The sum of sine series is", round(sum1, 2))  
