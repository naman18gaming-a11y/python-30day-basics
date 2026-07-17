import pandas as pd
import plotly.express as px

# Create hospital dataset
hospital = pd.DataFrame({
    "Patient": ["John Doe", "Jane Roe", "Sam Lee", "Priya Sen", "Ali Khan", "Maria Das", "Chen Wu", "Ravi Iyer"],
    "Age": [25, 40, 33, 29, 55, 47, 38, 62],
    "Bill": [1200, 2500, 1800, 900, 4000, 2200, 1500, 5000],
    "Department": ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Oncology", "Cardiology", "Neurology", "Oncology"],
    "Tests": [5, 8, 6, 3, 10, 7, 4, 12]
})

fig = px.scatter(
    hospital,
    x="Age",
    y="Bill",
    color="Department",
    size="Tests",
    hover_name="Patient"
)
fig.show()