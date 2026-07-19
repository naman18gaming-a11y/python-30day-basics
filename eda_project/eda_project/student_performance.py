import kagglehub
import pandas as pd
import os
import seaborn as sns

path = kagglehub.dataset_download("spscientist/students-performance-in-exams")
csv_file = os.path.join(path, "StudentsPerformance.csv")
df = pd.read_csv(csv_file)


print("Rows:", df.shape[0])
print("coloumb",df.shape[1])
print("Column names:", df.columns.tolist())
print("data type:",df.dtypes)
print("missing values:",df.isnull().sum())
print("duplicated value:",df.duplicated().sum())
numeric_cols = df.select_dtypes(include=['int64','float64']).columns
print("Numeric columns:", numeric_cols.tolist())
categorical_cols = df.select_dtypes(include=['object']).columns
print("Categorical columns:", categorical_cols.tolist())

df.info(memory_usage="deep")
df.columns=(
    df.columns
    .str.lower()
    .str.strip()
    .str.replace(" ","_")
)