import matplotlib.pyplot as plt
hours = [1,2,3,4,5]
marks = [50,60,70,80,90]
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)

plt.plot(hours, marks)

plt.title("Line")

plt.subplot(1,2,2)

plt.bar(hours, marks)

plt.title("Bar")

plt.show()