import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6, 7]
marks = [55, 60, 68, 75, 80, 88, 95]

plt.figure(figsize=(15, 5))

# Subplot 1: Line plot
plt.subplot(1, 3, 1)
plt.plot(hours, marks, color="red")
plt.title("Line Plot")
plt.xlabel("Hours")
plt.ylabel("Marks")

# Subplot 2: Scatter plot
plt.subplot(1, 3, 2)
plt.scatter(hours, marks, color="red")
plt.title("Scatter Plot")
plt.xlabel("Hours")
plt.ylabel("Marks")

# Subplot 3: Histogram
plt.subplot(1, 3, 3)
plt.hist(marks, bins=5, color="red", edgecolor="black")
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()