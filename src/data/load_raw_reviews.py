from __future__ import annotations

import gzip
import json
from pathlib import Path

import pandas as pd


RETAINED_COLUMNS = [
    "asin",
    "reviewText",
    "overall",
    "summary",
    "unixReviewTime",
    "reviewTime",
    "verified",
    "vote",
]


def load_raw_reviews(file_path: Path) -> pd.DataFrame:
    """Load selected fields from the compressed raw review file."""
    records = []

    with gzip.open(file_path, "rt", encoding="utf-8") as file:
        for line in file:
            review = json.loads(line)
            records.append(
                {
                    column: review.get(column)
                    for column in RETAINED_COLUMNS
                }
            )

    return pd.DataFrame(records)


if __name__ == "__main__":
    raw_file = Path("data/raw/Video_Games_5.json.gz")
    reviews = load_raw_reviews(raw_file)

    print(f"Loaded rows: {len(reviews):,}")
    print(f"Loaded columns: {reviews.columns.tolist()}")