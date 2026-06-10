# write a file 
with open("data.txt", "w") as file:
    name =  input("enter your name:")
    age = input("enter your age:")
    school = input("enter the name of the school")
    file.write("age: " + age + "\n")
    file.write("Name: " + name + "\n")
    file.write("School: " + school + "\n")