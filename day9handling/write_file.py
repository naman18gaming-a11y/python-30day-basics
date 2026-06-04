# write a file 
with open("data.txt", "w") as file:
    name =  input("enter your name:")
    file.write("Name: " + name + "\n")