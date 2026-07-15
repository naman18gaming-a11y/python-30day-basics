import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

students = pd.DataFrame({
    "Name": ["Naman", "Rahul", "Priya", "Aman", "Riya", "Arjun", "Simran", "Karan"],
    "Marks": [95, 82, 91, 76, 88, 79, 84, 93],
    "Hours": [8, 6, 7, 4, 6, 5, 6, 8],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi", "Pune", "Delhi"]
})

sns.set_theme(style="whitegrid", palette="deep")

# Bar plot
plt.figure(figsize=(12, 8))
sns.barplot(
    x="City",
    y="Marks",
    data=students,
    color="blue",
)
plt.title("Average marks by category", fontsize=16, fontweight="bold")
plt.savefig("barplot.png", dpi=300)
plt.tight_layout()
sns.despine()
plt.show()

# Box plot
plt.figure(figsize=(12, 8))
sns.boxplot(
    x="Marks",
    y="City",
    data=students,
    linewidth=2,
    width=0.5
)
plt.title("Marks by city", fontsize=16, fontweight="bold")
plt.tight_layout()
sns.despine()
plt.show()

# Violin plot
plt.figure(figsize=(12, 8))
sns.violinplot(
    x="Marks",
    y="City",
    data=students,
    linewidth=2,
    width=0.5,
)
plt.title("Marks by city in violin", fontsize=16, fontweight="bold")
plt.tight_layout()
sns.despine()
plt.show()

#swarmp plot 
plt.figure(figsize=(12,8))
sns.swarmplot(
    x="Marks",
    y="City",
    data= students,
    linewidth=2,
   
)
plt.title("marks by city swarmp plot",fontsize = 16, fontweight="bold")
plt.tight_layout()
sns.despine()
plt.show()

