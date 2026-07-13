import matplotlib.pyplot as plt
days = ["Mon","Tue","Wed","Thu","Fri"]
patients = [120,145,138,160,175]
plt.plot(
    days,
    patients,
    marker = "o",
    linestyle = "dashed",
    color = "blue",
    label = "patients"
)
plt.xlabel("Days")
plt.ylabel("Patients")
plt.title("Patients per Day")
plt.grid(True)
plt.show()