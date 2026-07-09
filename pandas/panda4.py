import pandas as pd

data = {
     "Name":["Naman","Rahul","Priya"],
    "Age":[20,21,19],
    "Marks":[95,88,91]
}
df = pd.DataFrame(data)
print(df.describe())