import pandas as pd
import plotly.express as px

students = pd.DataFrame({
    "Name":["Naman","Rahul","Priya","Aman","Riya","Arjun","Simran","Karan"],
    "Marks":[95,82,91,76,88,79,84,93],
    "Hours":[8,6,7,4,6,5,6,8],
    "City":["Delhi","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune","Delhi"]
})
fig = px.line(
    students,
    x = "Name",
    y="Marks",
    title="Marks of Students"
)
fig.show()