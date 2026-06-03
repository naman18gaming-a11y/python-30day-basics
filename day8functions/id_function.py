# Student ID function
def student_id():
    name = input("Enter the name: ")
    branch = input("Enter the branch: ")
    semester = input("Enter the semester: ")

    print("The name is:", name)
    print("The branch is:", branch)
    print("The semester is:", semester)
    print("The ID is:", name, branch, semester)

student_id()
