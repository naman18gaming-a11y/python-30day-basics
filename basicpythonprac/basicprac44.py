#Python Program to Find the Gravitational Force between Two Objects
m1 = float(input("enter the mass of object 1: "))
m2 =float(input("enter the mass of object 2: "))
r = int(input("enter the distance between the two objects: "))
g = 6.67 * 10**-11
force = g * m1 * m2 / r**2
print("The gravitational force between the two objects is:", force)