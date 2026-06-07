#Use reduce() to find the largest number in:
num = [10,45,90,23]
from functools import reduce

# Use reduce with the built-in max to find the largest number
largest = reduce(max, num)
print(largest)