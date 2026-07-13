import matplotlib.pyplot as plt 
students = ["Naman", "Rahul", "Priya", "Aman"]
marks = [95, 88, 91, 76]
plt.bar(students,marks, color = "orange")
plt.xlabel("students")
plt.ylabel("marks")
plt.title("students marks")
plt.show()