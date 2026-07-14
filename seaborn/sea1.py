import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

students = pd.DataFrame({

"Name":["Naman","Rahul","Priya","Aman","Riya"],

"Marks":[95,82,91,76,88],

"Hours":[8,6,7,4,6],

"City":["Delhi","Mumbai","Delhi","Pune","Mumbai"]

})
sns.lineplot(
    x="Name",
    y ="Marks",
    data = students
)
plt.show()