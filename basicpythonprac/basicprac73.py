#Python Program to Find Second Largest Number in a List
l = [int(x)for x in input("enter a number separated by space: ")]
l.sort()
print("second largest number:", l[-2])