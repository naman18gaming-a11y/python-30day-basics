import pandas as pd
data ={
        "Name": ["Naman", "Rahul", "Priya", "Aman"],
    "Age": [20, 21, 19, 22],
    "Marks": [95, 88, 91, 76],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune"]
}
df = pd.DataFrame(data)
print(df)
print(df[df["City"]== "Pune"])
