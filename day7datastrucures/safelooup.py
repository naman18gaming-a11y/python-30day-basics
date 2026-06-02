# safe lock
student = {
    "name": "Naman",
    "age": 20
}
print("Name:", student["name"])
print("Age:", student["age"])
phone = student.get("phone", " Not Available")
print("Phone:", phone)