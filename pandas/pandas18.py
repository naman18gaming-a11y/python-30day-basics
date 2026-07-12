import pandas as pd
import pandas as pd

students = pd.DataFrame({
    "student_ID":[101,102,103,104],
    "name":["Naman","Rahul","Priya","Aman"],
    "city":["Delhi","Mumbai","Delhi","Pune"]
})

marks = pd.DataFrame({
    "student_ID":[101,102,103,105],
    "marks":[95,88,91,75]
})
df = pd.merge(students, marks, on = "student_ID", how = "outer")
print(df)