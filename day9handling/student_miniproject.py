import json

def add_student():
    try:
        name = input("Enter the name of the student: ")
        age = int(input("Enter the age of the student: "))   # convert to int safely
        marks = int(input("Enter the marks of the student: "))

        student = {"name": name, "age": age, "marks": marks}

        # Load existing data if file exists
        try:
            with open("student.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []   # start fresh if file not found
        except json.JSONDecodeError:
            data = []   # start fresh if file is empty/corrupted

        # Append new student
        data.append(student)

        # Save back to file
        with open("student.json", "w") as file:
            json.dump(data, file, indent=4)

        print("✅ Student record added successfully!")

    except ValueError:
        print("❌ Invalid input! Age and marks must be numbers.")


def view_student():
    try:
        with open("student.json", "r") as file:
            data = json.load(file)
        print("\n--- Student Records ---")
        for student in data:
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            print("----------------------")
    except FileNotFoundError:
        print("❌ No student records found (file missing).")
    except json.JSONDecodeError:
        print("❌ Error reading student records (file corrupted).")


def search_student():
    name = input("Enter the name of the student to search: ")
    try:
        with open("student.json", "r") as file:
            data = json.load(file)
        found = False
        for student in data:
            if student["name"].lower() == name.lower():
                print("✅ Student Found:")
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Marks:", student["marks"])
                found = True
                break
        if not found:
            print("❌ Student not found.")
    except FileNotFoundError:
        print("❌ No student records found (file missing).")
    except json.JSONDecodeError:
        print("❌ Error reading student records (file corrupted).")


# Menu loop
while True:
    print("\n1. Add Student Record")
    print("2. View Student Records")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("👋 Exiting the program.")
        break
    else:
        print("❌ Invalid choice. Please try again.")
