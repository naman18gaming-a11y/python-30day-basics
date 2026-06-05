# create a json file
import json
student = {
    "name":"Naman",
    "age":20,
    "branch":"ECE"
}
with open ("student.json", "w") as file:
    json.dump(student, file)
print("JSON file 'student.json' created successfully!")
