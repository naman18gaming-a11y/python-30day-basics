#Python Program to Add a Key-Value Pair to the Dictionary
k=int(input("Enter the key (int) to be added:"))
v=int(input("Enter the value for the key to be added:"))
d={}
d.update({k:v})
print("Updated dictionary is:")
print(d)