# Functions for student marks analysis

def total_marks(marks):
    print("Total:", sum(marks))

def average_marks(marks):
    avg = sum(marks) / len(marks)
    print("Average:", avg)

def highest_marks(marks):
    print("Highest:", max(marks))

def lowest_marks(marks):
    print("Lowest:", min(marks))

def grade_calculator(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    print("Grade:", grade)


# Example dataset
marks = [85, 90, 78, 92, 88]

# Function calls
total_marks(marks)
average_marks(marks)
highest_marks(marks)
lowest_marks(marks)
grade_calculator(marks)
