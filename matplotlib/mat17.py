import matplotlib.pyplot as plt
ages = [
18,20,22,25,28,
35,38,40,42,
50,55,60,65
]
plt.hist(ages,bins=6,color="orange")
plt.title("the ages of the patients")
plt.show()