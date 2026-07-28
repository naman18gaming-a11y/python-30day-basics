#Python Program to Count Number of Uppercase and Lowercase Letters in a String
s = input("enter the string:")
count = 0
for char in s:
    if char.isupper() or char.islower():
        count += 1
print(count)
