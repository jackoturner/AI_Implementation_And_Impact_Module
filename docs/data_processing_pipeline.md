# Data Processing Log

## Dataset

- Dataset: UCSD Amazon Reviews - Video Games 5-core subset
- Raw records loaded: 497,577

## Cleaning steps

The pipeline:

1. Retained only fields relevant to this project.
2. Converted HTML entities and removed HTML tags from review text.
3. Normalised any repeated whitespace.
4. Removed missing or empty review text.
5. Converted ratings into numeric values.
6. Kept only ratings between one and five stars.
7. Converted review dates.
8. Removed duplicate records using product ID, review text, rating and review date.

## Result

- Cleaned records: 473,972
- Records removed: 23,605

## Sentiment labels

Sentiment labels are derived from product star ratings:

- 1-2 stars: negative
- 3 stars: neutral
- 4-5 stars: positive

## Modelling Sample

The complete cleaned dataset contains 473,972 reviews. A reproducible stratified sample of 100,000 reviews was created for model development and evaluation.

A fixed random state of 42 was used. Stratified sampling preserved the original sentiment proportions:

- Positive: 79.21%
- Negative: 10.97%
- Neutral: 9.82%

Using this sample keeps model training and cross-validation manageable while retaining a large, representative dataset for the three sentiment classes.