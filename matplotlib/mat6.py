import matplotlib.pyplot as plt
subjects = ["Python", "SQL", "Pandas", "NumPy"]
hours = [40, 25, 20, 15]
plt.bar(subjects,hours ,color ="green")
plt.xlabel("subjects")
plt.ylabel("hours")
plt.title("hours spend in each sub")
plt.show()