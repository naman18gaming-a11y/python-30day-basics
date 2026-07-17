
import plotly.express as px
import pandas as pd

students = pd.DataFrame({
    "Name":["Naman","Rahul","Priya","Aman","Riya","Arjun","Simran","Karan"],
    "Marks":[95,82,91,76,88,79,84,93],
    "Hours":[8,6,7,4,6,5,6,8],
    "City":["Delhi","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune","Delhi"]
})
fig = px.scatter(
    students,
    x ='Hours',
    y= "Marks",
    color="City",
    size = "Marks",
    hover_name="Name",
    title="Hours vs Marks"
)
fig.show()