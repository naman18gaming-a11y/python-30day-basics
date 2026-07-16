import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hospital = pd.DataFrame({
    "Age":[22,45,35,60,28,50,40,31,55,65,48,29],
    "Waiting_Time":[10,30,15,45,12,40,20,18,35,50,25,14],
    "Total_Bill":[500,2000,1200,3500,800,2800,1800,1500,3000,4200,2400,900],
    "Number_of_Tests":[1,4,2,6,1,5,3,2,5,7,4,2],
    "Department":[
        "Cardiology","Neurology","Orthopedic","Emergency","Cardiology",
        "Emergency","Orthopedic","Cardiology","Neurology","Emergency",
        "Orthopedic","Cardiology"
    ]
})

sns.set_theme(style="whitegrid")

# Jointplot
g = sns.jointplot(
    x='Age',
    y="Total_Bill",   
    data=hospital,
    kind="reg",
    height=6
)
g.fig.suptitle("AGE VS BILL")
g.fig.tight_layout()
g.fig.subplots_adjust(top=0.95)

# Displot
d = sns.displot(
    x="Waiting_Time",
    data=hospital,
    bins=6,
    kde=True,
)
d.fig.suptitle("Displot (Waiting Time)")

# Catplot
c = sns.catplot(
    data=hospital,
    x="Department",
    y="Total_Bill",  
    kind="bar",
    height=5,
    aspect=1.5,
)
c.set_xticklabels(rotation=20)
c.fig.suptitle("Catplot (Average Bill by Department)")
corr = hospital.corr(numeric_only=True)
sns.clustermap(
    corr,
    annot=True,
    cmap="coolwarm",
    figsize=(7,7)
)
plt.show()
