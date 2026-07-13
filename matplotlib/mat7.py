import matplotlib.pyplot as plt
subjects = ["Python", "SQL", "Pandas", "NumPy"]
hours = [40, 25, 20, 15]
plt.pie(hours, labels=subjects, colors=["green", "blue", "orange", "red"],autopct="%1.1f%%",startangle=80)
plt.show()