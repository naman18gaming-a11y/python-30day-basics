# appen your city name to the file 
with open("data.txt", "a") as file:
    city = input("enter the name of the city:")
    file.write("city :" + city + "\n")