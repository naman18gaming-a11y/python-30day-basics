"""Interactive Streamlit dashboard for the cleaned heart-disease dataset."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "heart_disease_cleaned.csv"
REPORT_PATH = PROJECT_DIR / "data" / "cleaning_report.json"

OUTCOME_COLORS = {
    "No heart disease": "#20A39E",
    "Heart disease": "#EF5B5B",
}

FEATURE_LABELS = {
    "age": "Age (years)",
    "trestbps": "Resting blood pressure (mm Hg)",
    "chol": "Cholesterol (mg/dL)",
    "thalach": "Maximum heart rate achieved",
    "oldpeak": "ST depression (oldpeak)",
    "ca": "Major vessels (0–4)",
}

DATA_DICTIONARY = [
    ("age", "Age", "Years"),
    ("sex", "Sex", "0 = female; 1 = male"),
    ("cp", "Chest-pain type", "0 = typical angina; 1 = atypical; 2 = non-anginal pain; 3 = asymptomatic"),
    ("trestbps", "Resting blood pressure", "mm Hg"),
    ("chol", "Serum cholesterol", "mg/dL"),
    ("fbs", "Fasting blood sugar", "1 = above 120 mg/dL; 0 = 120 mg/dL or lower"),
    ("restecg", "Resting ECG result", "0 = normal; 1 = ST-T wave abnormality; 2 = left ventricular hypertrophy"),
    ("thalach", "Maximum heart rate achieved", "Beats per minute"),
    ("exang", "Exercise-induced angina", "1 = yes; 0 = no"),
    ("oldpeak", "ST depression", "Exercise-induced depression relative to rest"),
    ("slope", "ST-segment slope", "0 = upsloping; 1 = flat; 2 = downsloping"),
    ("ca", "Major vessels", "Number coloured by fluoroscopy"),
    ("thal", "Thalassemia result", "0 = unknown; 1 = fixed defect; 2 = normal; 3 = reversible defect"),
    ("target", "Recorded outcome", "1 = heart disease; 0 = no heart disease"),
]


st.set_page_config(
    page_title="Heart Disease Explorer",
    page_icon="❤",
    layout="wide",
    initial_sidebar_state="expanded",
)


def add_page_style() -> None:
    """Apply a small visual layer while retaining Streamlit's accessible widgets."""
    st.markdown(
        """
        <style>
            .block-container { max-width: 1450px; padding-top: 2.4rem; padding-bottom: 3rem; }
            [data-testid="stMetric"] {
                background: rgba(31, 41, 55, 0.035);
                border: 1px solid rgba(31, 41, 55, 0.10);
                border-radius: 0.8rem;
                padding: 1rem;
            }
            [data-testid="stMetricLabel"] { font-size: 0.86rem; }
            .dashboard-note {
                border-left: 4px solid #20A39E;
                border-radius: 0.35rem;
                background: rgba(32, 163, 158, 0.08);
                padding: 0.8rem 1rem;
                margin: 0.35rem 0 1.25rem 0;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data(show_spinner="Loading the cleaned dataset…")
def load_data(path: str) -> pd.DataFrame:
    """Load the output created by clean_data.py."""
    return pd.read_csv(path)


@st.cache_data(show_spinner=False)
def load_report(path: str) -> dict:
    if not Path(path).exists():
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def percentage(value: float) -> str:
    return f"{value:.1%}"


def style_figure(figure: go.Figure, height: int = 360) -> go.Figure:
    """Keep every chart visually consistent and easy to scan."""
    figure.update_layout(
        height=height,
        margin=dict(l=15, r=15, t=50, b=15),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend_title_text="",
        hoverlabel=dict(namelength=-1),
    )
    figure.update_xaxes(showgrid=False)
    figure.update_yaxes(gridcolor="rgba(128,128,128,0.16)", zeroline=False)
    return figure


def risk_by_group(frame: pd.DataFrame, column: str) -> pd.DataFrame:
    """Calculate record counts and outcome rate for a readable category."""
    summary = (
        frame.groupby(column, dropna=False, observed=True)
        .agg(records=("target", "size"), heart_disease_rate=("target", "mean"))
        .reset_index()
    )
    summary["heart_disease_rate"] = summary["heart_disease_rate"] * 100
    return summary.sort_values("heart_disease_rate", ascending=False)


def rate_bar_chart(frame: pd.DataFrame, column: str, title: str) -> go.Figure:
    summary = risk_by_group(frame, column)
    figure = px.bar(
        summary,
        x=column,
        y="heart_disease_rate",
        text="heart_disease_rate",
        custom_data=["records"],
        color="heart_disease_rate",
        color_continuous_scale=["#D7EFEC", "#20A39E", "#EF5B5B"],
        labels={column: "", "heart_disease_rate": "Heart disease rate (%)"},
        title=title,
    )
    figure.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        hovertemplate="%{x}<br>Heart disease rate: %{y:.1f}%<br>Records: %{customdata[0]}<extra></extra>",
    )
    figure.update_layout(coloraxis_showscale=False)
    figure.update_yaxes(range=[0, max(100, summary["heart_disease_rate"].max() * 1.18)])
    return style_figure(figure)


def top_group_message(frame: pd.DataFrame, column: str, label: str) -> str:
    summary = risk_by_group(frame, column)
    top = summary.iloc[0]
    return (
        f"Within the current filters, **{top[column]}** has the highest recorded "
        f"heart-disease rate for {label}: **{top['heart_disease_rate']:.1f}%** "
        f"across {int(top['records'])} records."
    )


def filter_data(data: pd.DataFrame) -> pd.DataFrame:
    """Render sidebar filters and return the matching records."""
    with st.sidebar:
        st.header("Filter the cohort")
        st.caption("All charts and metrics update together.")

        outcome = st.radio(
            "Recorded outcome",
            options=["All records", "Heart disease", "No heart disease"],
        )
        sexes = st.multiselect(
            "Sex",
            options=sorted(data["sex_label"].unique()),
            default=sorted(data["sex_label"].unique()),
        )
        age_range = st.slider(
            "Age range",
            min_value=int(data["age"].min()),
            max_value=int(data["age"].max()),
            value=(int(data["age"].min()), int(data["age"].max())),
        )
        chest_pain = st.multiselect(
            "Chest-pain type",
            options=sorted(data["chest_pain_type"].unique()),
            default=sorted(data["chest_pain_type"].unique()),
        )

        st.divider()
        st.caption("Data source: Kaggle — johnsmith88/heart-disease-dataset")
        st.caption("For education and exploration only; this is not a diagnostic tool.")

    filtered = data.loc[
        data["sex_label"].isin(sexes)
        & data["age"].between(*age_range)
        & data["chest_pain_type"].isin(chest_pain)
    ].copy()
    if outcome != "All records":
        filtered = filtered.loc[filtered["outcome_label"] == outcome].copy()
    return filtered


def metric_row(frame: pd.DataFrame, total_records: int) -> None:
    """Show the most useful cohort indicators before detailed charts."""
    disease_rate = frame["target"].mean()
    exercise_angina_rate = (frame["exercise_angina"] == "Yes").mean()

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Unique records", f"{len(frame):,}", f"of {total_records:,} total")
    col2.metric("Recorded heart disease", percentage(disease_rate))
    col3.metric("Average age", f"{frame['age'].mean():.1f} years")
    col4.metric("Average cholesterol", f"{frame['chol'].mean():.0f} mg/dL")
    col5.metric("Exercise angina", percentage(exercise_angina_rate))


def overview_tab(frame: pd.DataFrame) -> None:
    st.subheader("Cohort overview")
    st.caption("How the recorded outcome is distributed across the selected patients.")

    left, right = st.columns((0.82, 1.18), gap="large")
    with left:
        outcome_counts = (
            frame["outcome_label"].value_counts().rename_axis("outcome_label").reset_index(name="records")
        )
        donut = px.pie(
            outcome_counts,
            names="outcome_label",
            values="records",
            hole=0.63,
            color="outcome_label",
            color_discrete_map=OUTCOME_COLORS,
            title="Recorded outcome split",
        )
        donut.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(style_figure(donut), width="stretch")

    with right:
        age_histogram = px.histogram(
            frame,
            x="age",
            color="outcome_label",
            nbins=max(8, min(16, frame["age"].nunique())),
            barmode="overlay",
            opacity=0.72,
            color_discrete_map=OUTCOME_COLORS,
            labels={"age": "Age (years)", "count": "Records"},
            title="Age distribution by recorded outcome",
        )
        st.plotly_chart(style_figure(age_histogram), width="stretch")

    left, right = st.columns(2, gap="large")
    with left:
        st.plotly_chart(
            rate_bar_chart(frame, "age_group", "Recorded heart-disease rate by age band"),
            width="stretch",
        )
    with right:
        st.plotly_chart(
            rate_bar_chart(frame, "sex_label", "Recorded heart-disease rate by sex"),
            width="stretch",
        )

    st.markdown(
        f"<div class='dashboard-note'>{top_group_message(frame, 'age_group', 'age band')} "
        "These are sample patterns, not a measure of an individual's risk.</div>",
        unsafe_allow_html=True,
    )


def risk_factors_tab(frame: pd.DataFrame) -> None:
    st.subheader("Risk-factor patterns")
    st.caption("Compare the share of each subgroup that has a recorded heart-disease outcome.")

    left, right = st.columns(2, gap="large")
    with left:
        st.plotly_chart(
            rate_bar_chart(frame, "chest_pain_type", "Outcome rate by chest-pain type"),
            width="stretch",
        )
    with right:
        st.plotly_chart(
            rate_bar_chart(frame, "exercise_angina", "Outcome rate by exercise-induced angina"),
            width="stretch",
        )

    left, right = st.columns(2, gap="large")
    with left:
        st.plotly_chart(
            rate_bar_chart(frame, "blood_pressure_category", "Outcome rate by resting blood-pressure band"),
            width="stretch",
        )
    with right:
        st.plotly_chart(
            rate_bar_chart(frame, "cholesterol_category", "Outcome rate by cholesterol band"),
            width="stretch",
        )

    scatter = px.scatter(
        frame,
        x="trestbps",
        y="chol",
        color="outcome_label",
        color_discrete_map=OUTCOME_COLORS,
        hover_data={
            "age": True,
            "sex_label": True,
            "chest_pain_type": True,
            "thalach": True,
            "trestbps": False,
            "chol": False,
        },
        labels={
            "trestbps": "Resting blood pressure (mm Hg)",
            "chol": "Cholesterol (mg/dL)",
        },
        title="Blood pressure and cholesterol for each record",
    )
    scatter.add_vline(x=140, line_dash="dot", line_color="#697386")
    scatter.add_hline(y=240, line_dash="dot", line_color="#697386")
    scatter.add_annotation(x=140, y=frame["chol"].max(), text="140 mm Hg", showarrow=False, yshift=12)
    scatter.add_annotation(x=frame["trestbps"].max(), y=240, text="240 mg/dL", showarrow=False, xshift=-35)
    st.plotly_chart(style_figure(scatter, height=430), width="stretch")
    st.caption(
        "Each dot is a de-duplicated record. The dotted reference lines are common screening thresholds, "
        "not a diagnosis or treatment recommendation."
    )

    st.markdown(
        f"<div class='dashboard-note'>{top_group_message(frame, 'chest_pain_type', 'chest-pain type')} "
        "Subgroup sizes are shown in chart tooltips; interpret small groups carefully.</div>",
        unsafe_allow_html=True,
    )


def clinical_patterns_tab(frame: pd.DataFrame) -> None:
    st.subheader("Clinical measurements")
    st.caption("Explore distributions and relationships without implying that correlation causes disease.")

    metric_options = list(FEATURE_LABELS)
    selected_metric = st.selectbox(
        "Distribution to compare by outcome",
        options=metric_options,
        index=4,
        format_func=lambda value: FEATURE_LABELS[value],
    )
    violin = px.violin(
        frame,
        x="outcome_label",
        y=selected_metric,
        color="outcome_label",
        box=True,
        points="all",
        color_discrete_map=OUTCOME_COLORS,
        labels={"outcome_label": "", selected_metric: FEATURE_LABELS[selected_metric]},
        title=f"{FEATURE_LABELS[selected_metric]} by recorded outcome",
    )
    st.plotly_chart(style_figure(violin, height=400), width="stretch")

    left, right = st.columns((1.12, 0.88), gap="large")
    with left:
        correlation_columns = list(FEATURE_LABELS) + ["target"]
        correlation = frame[correlation_columns].corr(numeric_only=True).round(2)
        labels = [FEATURE_LABELS.get(column, "Recorded outcome") for column in correlation.columns]
        heatmap = go.Figure(
            data=go.Heatmap(
                z=correlation.values,
                x=labels,
                y=labels,
                zmin=-1,
                zmax=1,
                colorscale="RdBu_r",
                colorbar=dict(title="Correlation"),
                text=correlation.values,
                texttemplate="%{text:.2f}",
                hovertemplate="%{x}<br>%{y}<br>Correlation: %{z:.2f}<extra></extra>",
            )
        )
        heatmap.update_layout(title="Correlation between numeric fields")
        st.plotly_chart(style_figure(heatmap, height=515), width="stretch")

    with right:
        summary = (
            frame.groupby("outcome_label", observed=True)[list(FEATURE_LABELS)]
            .median()
            .T.reset_index()
            .rename(columns={"index": "Measure"})
        )
        summary["Measure"] = summary["Measure"].map(FEATURE_LABELS)
        st.markdown("#### Median comparison")
        st.caption("A compact view of the middle value in each recorded outcome group.")
        st.dataframe(
            summary,
            hide_index=True,
            width="stretch",
            column_config={
                "Measure": st.column_config.TextColumn("Measure"),
                "Heart disease": st.column_config.NumberColumn("Heart disease", format="%.2f"),
                "No heart disease": st.column_config.NumberColumn("No heart disease", format="%.2f"),
            },
        )

    st.markdown("#### Build a custom scatter plot")
    x_col, y_col, _ = st.columns((1, 1, 1.4))
    with x_col:
        x_feature = st.selectbox(
            "X-axis", metric_options, index=1, format_func=lambda value: FEATURE_LABELS[value]
        )
    with y_col:
        y_feature = st.selectbox(
            "Y-axis", metric_options, index=3, format_func=lambda value: FEATURE_LABELS[value]
        )
    custom_scatter = px.scatter(
        frame,
        x=x_feature,
        y=y_feature,
        color="outcome_label",
        color_discrete_map=OUTCOME_COLORS,
        hover_data=["age", "sex_label", "chest_pain_type", "exercise_angina"],
        labels={x_feature: FEATURE_LABELS[x_feature], y_feature: FEATURE_LABELS[y_feature]},
        title=f"{FEATURE_LABELS[y_feature]} versus {FEATURE_LABELS[x_feature]}",
    )
    st.plotly_chart(style_figure(custom_scatter, height=430), width="stretch")


def records_tab(frame: pd.DataFrame) -> None:
    st.subheader("Inspect filtered records")
    st.caption("The download contains the cleaned numeric fields plus the readable label columns used in this dashboard.")

    default_columns = [
        "record_id",
        "outcome_label",
        "age",
        "sex_label",
        "chest_pain_type",
        "trestbps",
        "chol",
        "thalach",
        "exercise_angina",
        "oldpeak",
    ]
    available_columns = list(frame.columns)
    selected_columns = st.multiselect(
        "Columns to display",
        options=available_columns,
        default=[column for column in default_columns if column in available_columns],
    )
    if selected_columns:
        st.dataframe(
            frame[selected_columns].sort_values("record_id"),
            hide_index=True,
            width="stretch",
            height=440,
        )
    else:
        st.info("Choose at least one column to display the records.")

    download_data = frame.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download the filtered clean CSV",
        data=download_data,
        file_name="heart_disease_filtered_clean.csv",
        mime="text/csv",
        width="content",
    )


def data_quality_tab(frame: pd.DataFrame, report: dict) -> None:
    st.subheader("Data quality and definitions")
    st.caption("The dashboard uses only de-duplicated, validated rows from the downloaded CSV.")

    raw_rows = report.get("source_rows", "—")
    duplicates_removed = report.get("exact_duplicates_removed", "—")
    remaining_missing = report.get("remaining_missing_values", int(frame.isna().sum().sum()))

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Original rows", f"{raw_rows:,}" if isinstance(raw_rows, int) else raw_rows)
    col2.metric("Exact duplicates removed", f"{duplicates_removed:,}" if isinstance(duplicates_removed, int) else duplicates_removed)
    col3.metric("Clean rows", f"{len(frame):,}")
    col4.metric("Missing values remaining", remaining_missing)

    if report:
        st.markdown("#### Cleaning actions")
        notes: Iterable[str] = report.get("notes", [])
        for note in notes:
            st.write(f"• {note}")

        changes = []
        for title, key in [
            ("Non-numeric values converted", "non_numeric_values_converted_to_missing"),
            ("Invalid values or codes", "out_of_range_or_invalid_codes"),
            ("Values imputed", "values_imputed"),
        ]:
            values = report.get(key, {})
            changes.append(
                {
                    "Check": title,
                    "Fields affected": ", ".join(f"{field} ({count})" for field, count in values.items()) or "None",
                }
            )
        st.dataframe(pd.DataFrame(changes), hide_index=True, width="stretch")

    st.markdown("#### Data dictionary")
    dictionary = pd.DataFrame(DATA_DICTIONARY, columns=["Column", "Meaning", "Details / coding"])
    st.dataframe(dictionary, hide_index=True, width="stretch", height=470)


def main() -> None:
    add_page_style()
    st.title("Heart Disease Explorer")
    st.caption("An interactive view of the cleaned Kaggle heart-disease dataset")
    st.warning(
        "Educational data exploration only — the recorded target is not a medical diagnosis and this dashboard "
        "must not be used for clinical decisions.",
        icon="⚕️",
    )

    if not DATA_PATH.exists():
        st.error("The cleaned CSV is not available yet.")
        st.code("python clean_data.py\nstreamlit run app.py", language="bash")
        st.stop()

    data = load_data(str(DATA_PATH))
    filtered = filter_data(data)
    if filtered.empty:
        st.info("No records match these filters. Widen a sidebar selection to continue.")
        st.stop()

    metric_row(filtered, total_records=len(data))
    st.caption(f"Showing {len(filtered):,} of {len(data):,} unique, cleaned records.")

    overview, risk_factors, clinical, records, quality = st.tabs(
        ["Overview", "Risk patterns", "Clinical measures", "Records", "Data quality"]
    )
    with overview:
        overview_tab(filtered)
    with risk_factors:
        risk_factors_tab(filtered)
    with clinical:
        clinical_patterns_tab(filtered)
    with records:
        records_tab(filtered)
    with quality:
        data_quality_tab(filtered, load_report(str(REPORT_PATH)))


if __name__ == "__main__":
    main()
