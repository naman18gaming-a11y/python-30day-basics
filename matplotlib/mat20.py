import matplotlib.pyplot as plt

students = ["Naman", "Rahul", "Priya", "Aman", "Riya"]
marks = [95, 82, 91, 75, 88]
study_hours = [8, 6, 7, 4, 6]
subjects = ["Python", "SQL", "NumPy", "Pandas"]
hours_per_subject = [35, 25, 20, 20] 

plt.figure(figsize=(12, 8))

# 1. Line plot: Students vs Marks
plt.subplot(2, 2, 1)
plt.plot(students, marks, color="black", marker="o")
plt.title("Student Marks (Line Plot)")
plt.grid(True)

# 2. Pie chart: Hours per Subject
plt.subplot(2, 2, 2)
plt.pie(hours_per_subject, labels=subjects, autopct="%.1f%%", startangle=90)
plt.title("Subject Study Hours")

# 3. Bar plot: Students vs Marks

plt.subplot(2, 2, 3)
plt.bar(students, marks, color="blue")
plt.xlabel("Students") 
plt.ylabel("Marks")
plt.title("Student Scores (Bar Plot)")

# 4. Scatter plot: Study Hours vs Marks
plt.subplot(2, 2, 4)
plt.scatter(study_hours, marks, color="blue", s=120)
plt.title("Hours vs Marks (Scatter)")
plt.xlabel("Hours")
plt.ylabel("Marks")

plt.tight_layout()
plt.show()