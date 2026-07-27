"""Create a clean, dashboard-ready heart-disease dataset.

The source is the public Kaggle dataset ``johnsmith88/heart-disease-dataset``.
Run this file before launching the Streamlit dashboard.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd


DATASET_HANDLE = "johnsmith88/heart-disease-dataset"
PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT = PROJECT_DIR / "data" / "heart_disease_cleaned.csv"

EXPECTED_COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "target",
]

INTEGER_COLUMNS = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "slope",
    "ca",
    "thal",
    "target",
]

CATEGORICAL_COLUMNS = {
    "sex",
    "cp",
    "fbs",
    "restecg",
    "exang",
    "slope",
    "ca",
    "thal",
}

# These broad validation limits flag impossible codes or values without treating
# ordinary clinical variation as an error.
VALIDATION_RULES: dict[str, tuple[float, float] | set[int]] = {
    "age": (18, 100),
    "sex": {0, 1},
    "cp": {0, 1, 2, 3},
    "trestbps": (50, 300),
    "chol": (50, 700),
    "fbs": {0, 1},
    "restecg": {0, 1, 2},
    "thalach": (40, 250),
    "exang": {0, 1},
    "oldpeak": (0, 10),
    "slope": {0, 1, 2},
    "ca": {0, 1, 2, 3, 4},
    "thal": {0, 1, 2, 3},
    "target": {0, 1},
}

COLUMN_ALIASES = {
    "resting_blood_pressure": "trestbps",
    "resting_bp": "trestbps",
    "cholesterol": "chol",
    "fasting_blood_sugar": "fbs",
    "maximum_heart_rate": "thalach",
    "max_heart_rate": "thalach",
    "exercise_induced_angina": "exang",
    "number_of_major_vessels": "ca",
    "heart_disease": "target",
}

LABELS = {
    "sex": {0: "Female", 1: "Male"},
    "cp": {
        0: "Typical angina",
        1: "Atypical angina",
        2: "Non-anginal pain",
        3: "Asymptomatic",
    },
    "fbs": {0: "120 mg/dL or lower", 1: "Above 120 mg/dL"},
    "restecg": {
        0: "Normal",
        1: "ST-T wave abnormality",
        2: "Left ventricular hypertrophy",
    },
    "exang": {0: "No", 1: "Yes"},
    "slope": {0: "Upsloping", 1: "Flat", 2: "Downsloping"},
    "thal": {
        0: "Unknown / not recorded",
        1: "Fixed defect",
        2: "Normal",
        3: "Reversible defect",
    },
    "target": {0: "No heart disease", 1: "Heart disease"},
}


def normalise_column_name(column: object) -> str:
    """Convert a source header to a predictable snake_case name."""
    return str(column).strip().lower().replace("-", "_").replace(" ", "_")


def find_csv(source: Path) -> Path:
    """Find the most likely CSV inside a file or downloaded dataset directory."""
    if source.is_file():
        return source

    candidates = sorted(source.rglob("*.csv"))
    if not candidates:
        raise FileNotFoundError(f"No CSV file was found in: {source}")

    return next(
        (candidate for candidate in candidates if candidate.name.lower() == "heart.csv"),
        candidates[0],
    )


def download_source() -> Path:
    """Download the public Kaggle dataset and return the path to its CSV."""
    try:
        import kagglehub
    except ImportError as error:
        raise RuntimeError(
            "kagglehub is not installed. Run: python -m pip install kagglehub"
        ) from error

    dataset_path = Path(kagglehub.dataset_download(DATASET_HANDLE))
    return find_csv(dataset_path)


def invalid_value_mask(series: pd.Series, rule: tuple[float, float] | set[int]) -> pd.Series:
    """Return True for non-null values that violate a validation rule."""
    if isinstance(rule, set):
        return series.notna() & ~series.isin(rule)

    lower, upper = rule
    return series.notna() & ~series.between(lower, upper)


def add_readable_columns(frame: pd.DataFrame) -> pd.DataFrame:
    """Add labels and non-diagnostic groupings used by the dashboard."""
    enriched = frame.copy()
    enriched.insert(0, "record_id", range(1, len(enriched) + 1))

    enriched["outcome_label"] = enriched["target"].map(LABELS["target"])
    enriched["sex_label"] = enriched["sex"].map(LABELS["sex"])
    enriched["chest_pain_type"] = enriched["cp"].map(LABELS["cp"])
    enriched["fasting_blood_sugar"] = enriched["fbs"].map(LABELS["fbs"])
    enriched["resting_ecg"] = enriched["restecg"].map(LABELS["restecg"])
    enriched["exercise_angina"] = enriched["exang"].map(LABELS["exang"])
    enriched["st_slope"] = enriched["slope"].map(LABELS["slope"])
    enriched["thalassemia_result"] = enriched["thal"].map(LABELS["thal"])

    enriched["age_group"] = pd.cut(
        enriched["age"],
        bins=[0, 39, 49, 59, 69, float("inf")],
        labels=["Under 40", "40–49", "50–59", "60–69", "70+"],
        include_lowest=True,
    ).astype(str)
    enriched["cholesterol_category"] = pd.cut(
        enriched["chol"],
        bins=[0, 199, 239, float("inf")],
        labels=["Desirable (< 200)", "Borderline high (200–239)", "High (≥ 240)"],
        include_lowest=True,
    ).astype(str)
    enriched["blood_pressure_category"] = pd.cut(
        enriched["trestbps"],
        bins=[0, 119, 129, 139, float("inf")],
        labels=["Below 120", "120–129", "130–139", "140+"],
        include_lowest=True,
    ).astype(str)

    return enriched


def clean_heart_data(raw: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Standardise, validate, de-duplicate, and enrich the source data."""
    source_rows = len(raw)
    cleaned = raw.copy()
    cleaned.columns = [normalise_column_name(column) for column in cleaned.columns]
    cleaned = cleaned.rename(columns=COLUMN_ALIASES)

    missing_columns = sorted(set(EXPECTED_COLUMNS) - set(cleaned.columns))
    if missing_columns:
        raise ValueError(
            "The dataset is missing expected columns: " + ", ".join(missing_columns)
        )

    # Keep the dashboard schema stable if the source gains unrelated columns.
    cleaned = cleaned[EXPECTED_COLUMNS].dropna(how="all").copy()
    rows_after_empty_removal = len(cleaned)

    coercion_to_missing: dict[str, int] = {}
    for column in EXPECTED_COLUMNS:
        original = cleaned[column]
        numeric = pd.to_numeric(original, errors="coerce")
        coercion_to_missing[column] = int((original.notna() & numeric.isna()).sum())
        cleaned[column] = numeric

    invalid_values: dict[str, int] = {}
    for column, rule in VALIDATION_RULES.items():
        invalid = invalid_value_mask(cleaned[column], rule)
        invalid_values[column] = int(invalid.sum())
        cleaned.loc[invalid, column] = pd.NA

    # A missing outcome cannot be inferred safely. Other fields use a median or
    # most-common-value replacement so a valid row is not discarded needlessly.
    rows_dropped_missing_target = int(cleaned["target"].isna().sum())
    cleaned = cleaned.dropna(subset=["target"]).copy()

    imputed_values: dict[str, int] = {}
    for column in EXPECTED_COLUMNS:
        if column == "target":
            continue

        missing_count = int(cleaned[column].isna().sum())
        imputed_values[column] = missing_count
        if not missing_count:
            continue

        if column in CATEGORICAL_COLUMNS:
            replacement = cleaned[column].mode(dropna=True).iloc[0]
        else:
            replacement = cleaned[column].median(skipna=True)
        cleaned[column] = cleaned[column].fillna(replacement)

    for column in INTEGER_COLUMNS:
        cleaned[column] = cleaned[column].round().astype(int)
    cleaned["oldpeak"] = cleaned["oldpeak"].round(2)

    duplicates_removed = int(cleaned.duplicated().sum())
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)
    cleaned = add_readable_columns(cleaned)

    report: dict[str, Any] = {
        "dataset_handle": DATASET_HANDLE,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_rows": source_rows,
        "rows_after_blank_row_removal": rows_after_empty_removal,
        "rows_dropped_missing_target": rows_dropped_missing_target,
        "exact_duplicates_removed": duplicates_removed,
        "clean_rows": len(cleaned),
        "non_numeric_values_converted_to_missing": {
            column: count for column, count in coercion_to_missing.items() if count
        },
        "out_of_range_or_invalid_codes": {
            column: count for column, count in invalid_values.items() if count
        },
        "values_imputed": {
            column: count for column, count in imputed_values.items() if count
        },
        "remaining_missing_values": int(cleaned.isna().sum().sum()),
        "notes": [
            "Exact duplicate rows are removed before dashboard analysis.",
            "Invalid non-target values are replaced with a median (numeric) or mode (categorical) value.",
            "Invalid or missing target values are removed because outcomes are not inferred.",
            "A thal value of 0 is retained and labelled 'Unknown / not recorded'.",
        ],
    }
    return cleaned, report


def write_outputs(cleaned: pd.DataFrame, report: dict[str, Any], output_path: Path) -> Path:
    """Write the clean CSV and adjacent quality report."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cleaned.to_csv(output_path, index=False)

    report_path = output_path.with_name("cleaning_report.json")
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report_path


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean the Kaggle heart-disease CSV.")
    parser.add_argument(
        "--source",
        type=Path,
        help="Optional CSV file or directory. Without it, kagglehub downloads the dataset.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Clean CSV destination (default: {DEFAULT_OUTPUT}).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    source_csv = find_csv(args.source) if args.source else download_source()
    raw = pd.read_csv(source_csv)
    cleaned, report = clean_heart_data(raw)
    report_path = write_outputs(cleaned, report, args.output)

    print(f"Source CSV: {source_csv}")
    print(f"Clean CSV:  {args.output.resolve()}")
    print(f"Rows:       {report['source_rows']} -> {report['clean_rows']}")
    print(f"Duplicates removed: {report['exact_duplicates_removed']}")
    print(f"Report:     {report_path.resolve()}")


if __name__ == "__main__":
    main()
