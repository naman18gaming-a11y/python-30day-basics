#python Program to Count Number of Lowercase Characters in a String
s = input("enter a string:")
count = 0

for ch in s:
    if ch.islower():count += 1
print(count)