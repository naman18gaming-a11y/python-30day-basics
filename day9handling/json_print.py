#Read the JSON data and print:
import json
with open("student.json", "r")as file:
    data = json.load(file)
print("Name:", data["name"])