#Python Program to Check Prime Number
import math
def is_prime(i):
    if i < 1  :
        return False
    for num in range (2,math.sqrt(i)+1):
        if i % num ==0:
            return False
        return True
    