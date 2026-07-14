import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
hours=[2,3,2.5,4,3.5,5,4]
problems_solved=[1,2,2,3,3,4,5]
plt.figure(figsize=(15, 5))


# making  LINE plot 
plt.subplot(1, 3, 1)
plt.plot(hours,days,color="blue")
plt.xlabel("hours")
plt.ylabel("hours")
plt.title("Study hours")

#making PIE chart plot
plt.subplot(1, 3, 2)
plt.pie(hours,labels=days,autopct="%.1f%%")
plt.title("problem solved")

#making SCATTER plot
plt.subplot(1, 3, 3)
plt.scatter(hours,problems_solved)
plt.xlabel("problem solved")
plt.ylabel("hours")
plt.title("hours vs problems")
plt.tight_layout()
plt.show()


