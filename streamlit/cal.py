import streamlit as st

st.set_page_config(
    page_title="Calculator App",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Simple Calculator")
st.header("My First Streamlit Project")
st.write("Perform basic arithmetic operations using Streamlit.")

st.divider()

num1 = st.number_input("Enter the first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter the second number:", value=0.0, step=1.0)

operation = st.selectbox(
    "Select an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

if st.button("Calculate", key="calculate",use_container_width=True):
    if operation == "Addition":
        result = num1+num2
        st.success(f"Result = {result}")
    elif operation == "Subtraction":
        result = num1-num2
        st.success(f"Result = {result}")
elif operation == "Multiplication":
    result = num1*num2
    st.success(f"Result = {result}")
elif operation == "Division":
    if num2 != 0:
        result = num1/num2
        st.success(f"Result = {result}")
    else:
        st.error("Error: Division by zero is not allowed.")



st.divider()
st.caption("Made with ❤️ using Streamlit")