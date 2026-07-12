import pandas as pd
df = pd.read_csv("Sales_data.csv")

print(df.sort_values("Price"))

print(df.sort_values("Rating"))
print(df.sort_values("Price", ascending=False))