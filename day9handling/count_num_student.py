# count the number of students in the file
with open("students.csv", "r") as file:
    content = file.read()
    student_count = content.count("Name") - 1  # Subtract 1 for the header row
    print(f"Number of students: {student_count}")