#Python Program to Remove Duplicates from a List
l = [int(x) for x in input("enter numbers separated by space: ").split()]
unique_list = list(set(l))
print("List", unique_list)