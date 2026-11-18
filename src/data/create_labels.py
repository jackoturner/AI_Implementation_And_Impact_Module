from __future__ import annotations

import pandas as pd


def rating_to_sentiment(rating: float) -> str:
    """Map a valid one-to-five star rating to a sentiment label."""
    if rating <= 2:
        return "negative"

    if rating == 3:
        return "neutral"

    return "positive"


def add_sentiment_labels(reviews: pd.DataFrame) -> pd.DataFrame:
    """Add a sentiment column derived from the star-rating field."""
    labelled = reviews.copy()

    labelled["sentiment"] = labelled["overall"].apply(
        rating_to_sentiment
    )

    return labelled