import pandas as pd
data = {
    "Name": ["Naman", "Rahul", "Priya", "Aman", "Riya", "Arjun"],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Delhi"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Marks": [95, 88, 91, 76, 84, 79],
    "Salary": [50000, 45000, 55000, 60000, 47000, 52000]
}
df=pd.DataFrame(data)
print(df["City"].value_counts())
