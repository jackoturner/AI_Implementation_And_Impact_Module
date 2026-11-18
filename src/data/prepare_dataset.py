from __future__ import annotations

import json
from pathlib import Path

from src.data.clean_reviews import clean_reviews
from src.data.create_labels import add_sentiment_labels
from src.data.load_raw_reviews import load_raw_reviews


RAW_DATA_PATH = Path("data/raw/Video_Games_5.json.gz")
PROCESSED_DATA_PATH = Path(
    "data/processed/video_games_reviews_cleaned.csv"
)
SUMMARY_PATH = Path(
    "data/processed/processing_summary.json"
)


def main() -> None:
    raw_reviews = load_raw_reviews(RAW_DATA_PATH)
    cleaned_reviews = clean_reviews(raw_reviews)
    labelled_reviews = add_sentiment_labels(cleaned_reviews)

    PROCESSED_DATA_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    labelled_reviews.to_csv(
        PROCESSED_DATA_PATH,
        index=False,
    )

    summary = {
        "raw_rows": len(raw_reviews),
        "cleaned_rows": len(cleaned_reviews),
        "labelled_rows": len(labelled_reviews),
        "removed_rows": len(raw_reviews) - len(cleaned_reviews),
    }

    SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )

    print("Dataset preparation complete.")
    print(json.dumps(summary, indent=2))
    print(f"Saved dataset to: {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    main()