import pandas as pd

df = pd.read_csv("Sales_data.csv")
print(df.columns)
data = df[["Customer", "Product", "Price"]]
print(data)


