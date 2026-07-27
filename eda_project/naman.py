import streamlit as st
import pandas as pd
import numpy as np

st.title("Practice Dashboard ✅")

# Generate sample data
df = pd.DataFrame({
    "x": np.arange(1, 11),
    "y": np.random.randint(10, 100, 10)
})

# Show table
st.subheader("Sample Data")
st.dataframe(df)

# Show chart
st.subheader("Line Chart")
st.line_chart(df.set_index("x"))
