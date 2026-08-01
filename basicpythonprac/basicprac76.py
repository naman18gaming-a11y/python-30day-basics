#Python Program to Find Average of a List
l1 = [int(x) for x in input("Enter numbers separated by space: ").split()]
l2 = [int(x) for x in input("Enter numbers 2 separated by space: ").split()]
l3 = [int(x) for x in input("Enter numbers 3 separated by space: ").split()]

for lst in [l1, l2, l3]:
    if len(lst) > 0:
        avg = sum(lst) / len(lst)
        print("Average:", avg)
    else:
        print("List is empty, cannot compute average")
