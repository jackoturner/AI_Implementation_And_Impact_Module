# Dataset selection

For this project, I plan to use the Video Games category from the UCSD Amazon Reviews dataset.

It contains product reviews, star ratings, review dates and product identifiers. This should allow me to investigate sentiment classification using review text.

I selected this dataset because it is publicly available, has a clear source, and is relevant to an e-commerce sentiment dashboard.

The star rating may be used to create sentiment labels:

- 1-2 stars: negative
- 3 stars: neutral
- 4-5 stars: positive

Before using the dataset, I will inspect its quality, check for missing values and duplicates, and review whether the label groups are balanced.

## Planned dataset file

I will use the Video Games 5-core subset rather than the complete Video Games category. The full category is too large for local experimentation.

The 5-core subset is still large enough for this project. However, because it only includes users and products with at least five reviews, it may not represent all reviews equally. I will consider this limitation during the evaluation and ethical analysis.