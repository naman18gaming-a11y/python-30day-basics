import pandas as pd
df = pd.read_csv("sales_data.csv")
print(df.head())
print(df.describe())
print(df.shape)
print(df.columns)