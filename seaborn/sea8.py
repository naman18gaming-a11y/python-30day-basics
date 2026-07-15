import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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
sns.regplot(
    data = students,
    x ="Hours",
    y = "Marks"
)
plt.show()

