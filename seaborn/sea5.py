import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

students = pd.DataFrame({
    "Name":["Naman","Rahul","Priya","Aman","Riya","Arjun","Simran"],
    "Marks":[95,82,91,76,88,79,84],
    "Hours":[8,6,7,4,6,5,6],
    "City":["Delhi","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune"]
})

sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

sns.lineplot(x="Name", y="Marks", data=students, marker="o", ax=axes[0,0])
axes[0,0].set_title("Student vs Marks")

sns.scatterplot(x="Hours", y="Marks", hue="City", s=100, data=students, ax=axes[0,1])
axes[0,1].set_title("Hours vs Marks")

sns.histplot(students["Marks"], bins=5, color="skyblue", kde=True, ax=axes[1,0])
axes[1,0].set_title("Distribution of Marks")

sns.countplot(x="City", data=students, palette="Set2", ax=axes[1,1])
axes[1,1].set_title("Students by City")

plt.tight_layout()
plt.show()
