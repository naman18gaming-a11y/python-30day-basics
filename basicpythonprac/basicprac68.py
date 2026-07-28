#Python Program to Find Common Characters in Two Strings
s1= input("enter first string:")
s2= input("enter second string:")
for char in s1:
    if char in s2:
        print(char)