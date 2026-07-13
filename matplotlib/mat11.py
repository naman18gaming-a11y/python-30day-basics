import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
marks = [50,60,70,80,90]

plt.scatter(hours, marks)

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours vs Marks")
plt.scatter(
    hours,
    marks,
    color= "red",
    marker="o",
    s=120
)

plt.show()