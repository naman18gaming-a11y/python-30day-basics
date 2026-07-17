import pandas as pd
import plotly.express as px

students = pd.DataFrame({
    "Name":["Naman","Rahul","Priya","Aman","Riya","Arjun","Simran","Karan","Neha","Rohit"],
    "Marks":[95,82,91,76,88,79,84,93,86,90],
    "Hours":[8,6,7,4,6,5,6,8,7,7],
    "City":["Delhi","Mumbai","Delhi","Pune","Mumbai","Delhi","Pune","Delhi","Mumbai","Delhi"],
    "Gender":["Male","Male","Female","Male","Female","Male","Female","Male","Female","Male"]
})
fig = px.histogram(
    students,
    x="Marks",
    nbins=5,
    title ="distribution of marks"
)
fig.show()