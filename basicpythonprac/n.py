# main.py
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from io import BytesIO

st.set_page_config(page_title="Professional Dashboard", layout="wide", initial_sidebar_state="expanded")

# -------------------------
# Helpers and Sample Data
# -------------------------
@st.cache_data
def make_sample_data(n=2000, seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2024-01-01", periods=n, freq="H")
    categories = rng.choice(["Alpha", "Beta", "Gamma", "Delta"], size=n, p=[0.35,0.30,0.20,0.15])
    values = np.round(rng.normal(loc=120, scale=40, size=n).clip(min=0), 2)
    region = rng.choice(["North", "South", "East", "West"], size=n)
    users = rng.integers(1000, 2000, size=n)
    df = pd.DataFrame({
        "timestamp": dates,
        "category": categories,
        "region": region,
        "value": values,
        "users": users
    })
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    return df

def to_csv_bytes(df: pd.DataFrame) -> bytes:
    return df.to_csv(index=False).encode("utf-8")

# -------------------------
# Sidebar Controls
# -------------------------
st.sidebar.header("Data Source")
data_source = st.sidebar.radio("Choose data", ("Sample data", "Upload CSV"))

if data_source == "Sample data":
    rows = st.sidebar.slider("Sample rows", 500, 5000, 2000, step=100)
    df = make_sample_data(rows)
else:
    uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded)
            # Try to parse timestamp-like columns
            for col in ["timestamp", "datetime", "date", "time"]:
                if col in df.columns:
                    try:
                        df["timestamp"] = pd.to_datetime(df[col])
                        break
                    except Exception:
                        continue
            if "timestamp" not in df.columns:
                # create synthetic timestamp if none present
                df["timestamp"] = pd.date_range("2024-01-01", periods=len(df), freq="H")
            df["date"] = pd.to_datetime(df["timestamp"]).dt.date
            df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
            # Ensure numeric columns exist
            if "value" not in df.columns:
                df["value"] = pd.to_numeric(df.select_dtypes(include=[np.number]).iloc[:,0], errors="coerce").fillna(0)
            if "category" not in df.columns:
                df["category"] = "Unknown"
            if "region" not in df.columns:
                df["region"] = "Unknown"
        except Exception as e:
            st.sidebar.error("Could not read CSV. Upload a valid CSV file.")
            st.stop()
    else:
        st.sidebar.info("Upload a CSV or choose Sample data to continue.")
        st.stop()

# -------------------------
# Top KPIs
# -------------------------
st.title("Professional Streamlit Dashboard")
st.markdown("Interactive dashboard with upload, filters, charts, and export.")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Rows", f"{len(df):,}")
kpi2.metric("Unique Categories", df["category"].nunique() if "category" in df.columns else "N/A")
kpi3.metric("Average Value", f"{df['value'].mean():.2f}")
kpi4.metric("Unique Regions", df["region"].nunique() if "region" in df.columns else "N/A")

st.markdown("---")

# -------------------------
# Filters
# -------------------------
with st.expander("Filters", expanded=True):
    c1, c2, c3 = st.columns(3)
    categories = ["All"] + sorted(df["category"].unique().tolist())
    selected_cat = c1.selectbox("Category", categories, index=0)
    regions = ["All"] + sorted(df["region"].unique().tolist())
    selected_region = c2.selectbox("Region", regions, index=0)
    min_date = pd.to_datetime(df["date"].min())
    max_date = pd.to_datetime(df["date"].max())
    date_range = c3.date_input("Date range", [min_date, max_date])

# Apply filters
mask = pd.Series(True, index=df.index)
if selected_cat != "All":
    mask &= df["category"] == selected_cat
if selected_region != "All":
    mask &= df["region"] == selected_region
if isinstance(date_range, list) and len(date_range) == 2:
    start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    mask &= (pd.to_datetime(df["date"]) >= start.date()) & (pd.to_datetime(df["date"]) <= end.date())

filtered = df[mask].copy()

# -------------------------
# Layout: Charts and Table
# -------------------------
left, right = st.columns((2, 1))

with left:
    st.subheader("Time Series Overview")
    ts = filtered.groupby(pd.Grouper(key="timestamp", freq="D")).agg(total_value=("value", "sum")).reset_index()
    if ts.empty:
        st.info("No data for selected filters.")
    else:
        line = alt.Chart(ts).mark_line(point=True).encode(
            x=alt.X("timestamp:T", title="Date"),
            y=alt.Y("total_value:Q", title="Total Value"),
            tooltip=[alt.Tooltip("timestamp:T", title="Date"), alt.Tooltip("total_value:Q", title="Total")]
        ).interactive()
        st.altair_chart(line, use_container_width=True)

    st.subheader("Category Breakdown")
    cat = filtered.groupby("category").agg(count=("value", "count"), avg_value=("value", "mean")).reset_index()
    if not cat.empty:
        bar = alt.Chart(cat).mark_bar().encode(
            x=alt.X("category:N", sort="-y", title="Category"),
            y=alt.Y("count:Q", title="Count"),
            color=alt.Color("avg_value:Q", title="Avg Value", scale=alt.Scale(scheme="tealblues")),
            tooltip=["category", "count", alt.Tooltip("avg_value:Q", format=".2f")]
        )
        st.altair_chart(bar, use_container_width=True)

with right:
    st.subheader("Hourly Heatmap")
    heat = filtered.groupby(["hour", "category"]).agg(total=("value", "sum")).reset_index()
    if not heat.empty:
        heat_chart = alt.Chart(heat).mark_rect().encode(
            x=alt.X("hour:O", title="Hour"),
            y=alt.Y("category:N", title="Category"),
            color=alt.Color("total:Q", title="Total Value"),
            tooltip=["hour", "category", alt.Tooltip("total:Q", format=".2f")]
        ).properties(height=360)
        st.altair_chart(heat_chart, use_container_width=True)

st.markdown("---")

# -------------------------
# Data Table and Export
# -------------------------
st.subheader("Data Preview")
st.dataframe(filtered.reset_index(drop=True).head(300), use_container_width=True)

csv_bytes = to_csv_bytes(filtered)
st.download_button("Download filtered CSV", data=csv_bytes, file_name="filtered_data.csv", mime="text/csv")

# -------------------------
# Quick Analysis Widget
# -------------------------
st.markdown("---")
st.subheader("Quick Aggregation")
col_a, col_b = st.columns(2)
with col_a:
    agg_func = st.selectbox("Aggregate function", ["sum", "mean", "median", "count"])
    group_by = st.selectbox("Group by column", ["category", "region", "hour"])
with col_b:
    run = st.button("Run")

if run:
    if group_by not in filtered.columns:
        st.error("Selected group by column not available.")
    else:
        if agg_func == "count":
            result = filtered.groupby(group_by).size().reset_index(name="count")
        else:
            result = filtered.groupby(group_by).agg(result_value=("value", agg_func)).reset_index()
        st.table(result.sort_values(result.columns[-1], ascending=False).head(20))

# -------------------------
# Notes and Tips
# -------------------------
st.markdown("### Notes")
st.markdown(
    "- Upload a CSV with columns like timestamp, category, value, region to use your own data.\n"
    "- Use the filters to narrow the dataset and then download the filtered CSV.\n"
    "- If charts do not appear, try `streamlit hello` to verify Streamlit installation and ensure Python 3.9–3.11 is used."
)
