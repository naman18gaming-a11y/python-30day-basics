#Python Program to Count the Number of Vowels in a String
vov = 'aeiouAEIOU'
s = input("enter a string:")
count = 0
for ch in s:
    if ch in vov:
        count += 1  
print(count)
