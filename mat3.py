import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [60, 70, 75, 85, 95]

plt.plot(
    days,
    marks,
    color="green",
    marker="o",
    linestyle="dashed",
    label="marks"
)

plt.title("Students marks")
plt.xlabel("Days")
plt.ylabel("Marks")
plt.legend()
plt.show()
