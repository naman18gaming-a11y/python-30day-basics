# count spaces in a string
str = input("enter the string:")
count = 0
for i in range(len(str)):
    if str[i] == " ":
        count += 1
print("the number of spaces in the string is:", count)