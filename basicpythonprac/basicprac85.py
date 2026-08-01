#Python Program to Find the Sum of All the Items in a Dictionary
upper = int(input("Enter the upper limit: "))
lowwer = int(input("Enter the lowwer limit: "))
sum = {x+x for x in range(upper, lowwer +1)}
print(sum)