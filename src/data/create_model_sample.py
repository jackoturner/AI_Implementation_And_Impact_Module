from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


SOURCE_DATA_PATH = Path(
    "data/processed/video_games_reviews_cleaned.csv"
)

MODEL_SAMPLE_PATH = Path(
    "data/processed/video_games_model_sample.csv"
)

MODEL_SAMPLE_SIZE = 100_000
RANDOM_STATE = 42


def main() -> None:
    reviews = pd.read_csv(
        SOURCE_DATA_PATH,
        usecols=["reviewText", "sentiment"],
        keep_default_na=False,
    )

    model_sample, _ = train_test_split(
        reviews,
        train_size=MODEL_SAMPLE_SIZE,
        stratify=reviews["sentiment"],
        random_state=RANDOM_STATE,
    )

    model_sample.to_csv(
        MODEL_SAMPLE_PATH,
        index=False,
    )

    print(f"Source rows: {len(reviews):,}")
    print(f"Sample rows: {len(model_sample):,}")
    print("\nSample class distribution:")
    print(
        model_sample["sentiment"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )


if __name__ == "__main__":
    main()