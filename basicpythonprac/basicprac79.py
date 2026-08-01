#Python Program to Find the Sum of Elements in a List using Recursion
num = [int(x) for x in input("Enter numbers separated by space: ").split()]
def recursive_sum(lst):
  if len(lst) == 0:
     return 0
  else:
     return lst[0]  + recursive_sum(lst[1:])
result = recursive_sum(num)