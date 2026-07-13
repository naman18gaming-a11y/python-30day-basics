import matplotlib.pyplot as plt
departments = [
    "Cardiology",
    "Neurology",
    "Orthopedic",
    "Emergency"
]

patients = [120,80,95,160]

plt.bar(
    departments,
    patients,
    color="orange"
)

plt.title("Patients by Department")

plt.xlabel("Department")

plt.ylabel("Patients")

plt.show()