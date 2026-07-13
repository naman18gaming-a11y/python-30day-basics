import matplotlib.pyplot as plt

subjects = ["Python", "SQL", "Pandas", "NumPy"]
hours = [40, 25, 20, 15]

# First pie chart (basic)
plt.pie(hours, labels=subjects, colors=["green", "blue", "orange", "red"])

# Exploded pie chart
explode = [0.1, 0, 0, 0]
plt.pie(
    hours,
    labels=subjects,
    explode=explode,
    autopct="%.1f%%"
)

plt.show()
