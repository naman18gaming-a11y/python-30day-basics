#Python Program to Split Even and Odd Elements into Two Lists
l = [int(x) for x in input("Enter numbers separated by space: ")]

even_l = []
odd_l = []

for num in l:
    if num % 2 == 0:
        even_l.append(num)
    else:
        odd_l.append(num)

print("Even list:", even_l)
print("Odd list:", odd_l)
