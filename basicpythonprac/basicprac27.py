#Python Program to Print All Possible Combinations of Three Digits
a = int(input("enter num 1:"))
b = int(input("enter num 2:"))
c = int(input("enter num 3:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])