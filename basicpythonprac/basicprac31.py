#Python Program to Print an Inverted Star Pattern
rows = 10
for i in range(rows, 0, -1):      
    for j in range(i):            
        print("*", end=" ")
    print()                        
