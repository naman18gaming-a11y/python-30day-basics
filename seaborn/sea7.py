import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
students = pd.DataFrame({
    "Name": ["Naman", "Rahul", "Priya", "Aman", "Riya",
             "Arjun", "Simran", "Karan", "Neha", "Rohit"],

    "Marks": [95, 82, 91, 76, 88,
              79, 84, 93, 89, 72],

    "Hours": [8, 6, 7, 4, 6,
              5, 6, 8, 7, 3],

    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai",
             "Delhi", "Pune", "Delhi", "Mumbai", "Pune"]
})
sns.set_theme(style="whitegrid", palette="Set2")
plt.figure(figsize=(14,10))

plt.subplot(2,2,1)

sns.barplot(
    data=students,
    x="City",
    y="Marks"
)

plt.title("Average Marks by City")
plt.subplot(2,2,2)

sns.scatterplot(
    data=students,
    x="Hours",
    y="Marks",
    s=120
)

plt.title("Study Hours vs Marks")
plt.subplot(2,2,3)

sns.histplot(
    students["Marks"],
    kde=True
)

plt.title("Distribution of Marks")
plt.subplot(2,2,4)

sns.boxplot(
    data=students,
    x="City",
    y="Marks"
)

plt.title("Marks Spread by City")
plt.tight_layout()

plt.savefig("student_dashboard.png", dpi=300)

plt.show()