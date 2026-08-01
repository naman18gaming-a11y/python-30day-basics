#Python Program to Merge Two Lists and Sort it
l1 = [int(x) for x in input("Enter numbers separated by space: ").split()]
l2 = [int(x) for x in input("Enter numbers 2 separated by space: ").split()]
merged_list = l1 + l2
sorted_list = sorted(merged_list)
print("Merged and Sorted List:", sorted_list)