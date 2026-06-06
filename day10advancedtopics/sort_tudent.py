#Lambda + sorted()
students = [
    ("Naman", 85),
    ("Rahul", 72),
    ("Aman", 95),
    ("Priya", 88)
]
sort = [sorted(students, key = lambda x: x[1]) ]
print(students)