import streamlit as st
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("📊 BMI Calculator")
st.header("calculate your Body Mass Index (BMI)")
st.write("Enter your weight and height to calculate your BMI.")
st.markdown("""
<style>
.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
    color:white;
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#60a5fa;
}

.sub-title{
    text-align:center;
    color:#d1d5db;
    font-size:18px;
    margin-bottom:30px;
}

.result-card{
    background:#1e293b;
    padding:25px;
    border-radius:15px;
    text-align:center;
    border:1px solid #334155;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="main-title">⚖️ BMI Calculator</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Calculate your Body Mass Index instantly.</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input(
        "enter your weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.5
    )

with col2:
    height = st.number_input(
        "enter your height (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1
    )
    st.divider()
  
if st.button("Calculate BMI", use_container_width=True):

    height_m = height / 100

    bmi = weight / (height_m ** 2)

    st.metric("Your BMI", f"{bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
        color = "🟡"

    elif bmi < 25:
        category = "Normal Weight"
        color = "🟢"

    elif bmi < 30:
        category = "Overweight"
        color = "🟠"

    else:
        category = "Obese"
        color = "🔴"

    st.success(f"{color} Category: {category}")

    progress = min(bmi / 40, 1.0)
    st.progress(progress)

    st.markdown(
        f"""
        <div class="result-card">
            <h2>{color} {category}</h2>
            <h1>{bmi:.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("BMI Categories"):
        st.write("""
| BMI | Category |
|------|----------|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal Weight |
| 25 - 29.9 | Overweight |
| 30 and above | Obese |
""")

st.divider()
st.caption("Built with ❤️ using Streamlit")

