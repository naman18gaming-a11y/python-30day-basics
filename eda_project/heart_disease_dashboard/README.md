# Heart Disease Explorer

A Streamlit dashboard for the Kaggle dataset [`johnsmith88/heart-disease-dataset`](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).

It turns the raw `heart.csv` into a clean, documented CSV and provides interactive filters, charts, record exploration, and a data-quality view.

## Run it

From this folder:

```powershell
python -m pip install -r requirements.txt
python clean_data.py
streamlit run app.py
```

The cleaner uses `kagglehub.dataset_download("johnsmith88/heart-disease-dataset")`, so the first run needs internet access. If you already downloaded the dataset, point the cleaner at the local CSV or its folder instead:

```powershell
python clean_data.py --source "path\to\heart.csv"
```

Then open the local URL printed by Streamlit (normally `http://localhost:8501`).

## What the cleaner does

- Standardises the expected column names and numeric types.
- Validates binary/categorical codes and broad plausible numeric ranges.
- Removes rows with a missing or invalid outcome; uses median/mode values only for other missing fields.
- Removes exact duplicate records.
- Keeps `thal = 0` as `Unknown / not recorded` rather than silently discarding it.
- Adds readable labels and non-diagnostic age, blood-pressure, and cholesterol bands.
- Saves `data/heart_disease_cleaned.csv` and `data/cleaning_report.json`.

For the downloaded version used here, the raw file has 1,025 rows and 723 exact duplicates. The cleaned CSV contains 302 unique records.

## Dashboard contents

- Cohort summary metrics and outcome, age, and sex charts.
- Chest-pain, exercise-angina, blood-pressure, and cholesterol pattern charts.
- A blood-pressure versus cholesterol scatter plot.
- Outcome distributions, a correlation heatmap, and a custom scatter plot.
- A filterable record table with CSV download.
- A transparent cleaning report and full data dictionary.

## Important note

This is an educational exploratory dashboard. It does not diagnose heart disease, estimate a person's risk, or replace professional medical advice.
