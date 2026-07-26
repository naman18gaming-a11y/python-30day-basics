#Python Program to Print an Identity Matrix
col = int(input("enter the number of columns:"))
row = int(input("enter the number of rows:"))
for i in range(row):
    for j in range(col):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()