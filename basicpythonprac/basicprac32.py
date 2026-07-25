#Python Program to Print Pascal Triangle
rows = 6
for i in range(rows):
    print(" "*(rows-i),end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
