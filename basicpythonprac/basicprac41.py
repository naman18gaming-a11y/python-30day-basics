#Python Program to Clear the Rightmost Set Bit of a Number
# Python Program to Clear the Rightmost Set Bit

num = int(input("Enter a number: "))

# Clear the rightmost set bit
result = num & (num - 1)

print("Original number:", num)
print("After clearing rightmost set bit:", result)
