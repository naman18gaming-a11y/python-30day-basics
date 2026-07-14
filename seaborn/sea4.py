import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

students = pd.DataFrame({
    "Name":["Naman","Rahul","Priya","Aman","Riya"],
    "Marks":[95,82,91,76,88],
    "Hours":[8,6,7,4,6],
    "City":["Delhi","Mumbai","Delhi","Pune","Mumbai"]
})

plt.figure(figsize=(6,4))  # make the plot bigger
sns.countplot(
    x="City",
    data=students,
    palette="Set2"  # add some nice colors
)
sns.set_style("darkgrid")

plt.title("Number of Students per City")   # add title
plt.xlabel("City")                         # label x-axis
plt.ylabel("Count")                        # label y-axis
plt.show()
