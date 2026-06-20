#Python Program to Find Prime Numbers in a Given Range
num = int(input("enter the upper limit:"))
for a in range(2,num+1):
    k=0
    for i in range (2,a//2+1):
        if(a%i==0):
            k = k+1
            if(k<=0):
                print(a) 