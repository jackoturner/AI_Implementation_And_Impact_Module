from __future__ import annotations

import html
import re

import pandas as pd


DUPLICATE_COLUMNS = [
    "asin",
    "reviewText",
    "overall",
    "reviewTime",
]


def clean_review_text(value: object) -> str:
    """Standardise one review-text value."""
    if not isinstance(value, str):
        return ""

    text = html.unescape(value)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def clean_reviews(reviews: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw review records."""
    cleaned = reviews.copy()

    cleaned["reviewText"] = cleaned["reviewText"].apply(clean_review_text)
    cleaned["overall"] = pd.to_numeric(
        cleaned["overall"],
        errors="coerce",
    )
    cleaned["reviewTime"] = pd.to_datetime(
        cleaned["reviewTime"],
        errors="coerce",
    )

    cleaned = cleaned.dropna(
        subset=["reviewText", "overall"]
    )
    cleaned = cleaned[
        cleaned["reviewText"].str.len() > 0
    ]
    cleaned = cleaned[
        cleaned["overall"].between(1, 5)
    ]

    available_duplicate_columns = [
        column
        for column in DUPLICATE_COLUMNS
        if column in cleaned.columns
    ]

    cleaned = cleaned.drop_duplicates(
        subset=available_duplicate_columns
    )

    return cleaned.reset_index(drop=True)