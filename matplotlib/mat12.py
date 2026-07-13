import matplotlib.pyplot as plt
marks = [
80,82,84,86,
90,91,92,
70,71,
65,
95,96
]
plt.hist(marks,bins=5,color="green")
plt.figure(figsize=(8,5))
plt.show()