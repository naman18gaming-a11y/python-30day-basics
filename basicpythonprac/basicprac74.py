#Python Program to Print Largest Even and Largest Odd Number in a List
l = [int(x) for x in input("Enter numbers separated by space: ")]
sorted_list = sorted(l)
largest_even = None
largest_odd = None
for num in l:
    if num % 2 == 0:
        print("even:", num)
        if largest_even is None or num > largest_even:
            largest_even = num
    else:
        print("odd:", num)
        if largest_odd is None or num > largest_odd:
            largest_odd = num

print("Sorted list:", sorted_list)
print("Largest even:", largest_even)
print("Largest odd:", largest_odd)