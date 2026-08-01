#Python Program to Print Sum of Negative Numbers, Positive Even & Odd Numbers in a List
num = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
neg_sum = sum(x for x in num if x < 0)
pos_even_sum = sum(x for x in num if x > 0 and x % 2 == 0)
pos_odd_sum = sum(x for x in num if x > 0 and x %  2 != 0)
print("Sum of negative numbers:", neg_sum)
print("Sum of positive even numbers:", pos_even_sum)
print("Sum of positive odd numbers:", pos_odd_sum)