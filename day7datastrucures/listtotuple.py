# list to tuples
students = [
    ("Naman", 88),
    ("Rahul", 75),
    ("Aman", 91)
]
print(tuple(students))

for name, marks in students:
    print(name, "->", marks)