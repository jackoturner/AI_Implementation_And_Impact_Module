# E-Commerce Sentiment Analytics Dashboard

## CMP-X316-0 coursework implementation plan

This repository will contain a reproducible supervised-machine-learning project and software application. The project will analyse e-commerce product reviews, predict sentiment, compare models, and present the results in a dashboard.

> **Proposed problem:** A business receives too many product reviews to inspect manually. This system classifies submitted review text as negative, neutral, or positive and presents aggregate sentiment patterns to support human review. It is not an autonomous decision-making system.

## What this project must demonstrate

- A suitable, verifiable, non-synthetic dataset and a documented original-data link and processed-data link.
- Meaningful data preparation, including missing/inconsistent data, duplicates/irrelevant attributes, feature encoding/scaling where needed, and basic visualisations.
- Three supervised ML models, appropriate parameter tuning, and k-fold cross-validation.
- Suitable metrics compared across models and critical interpretation of results.
- A software application with input UI, results UI, workflow/business rules and authentication, plus an API connected to the selected ML model.
- A PDF report covering the required introduction, setup, results, comparison, ethics, reflection, references, and an honest AI-use declaration.
- A final ZIP with the PDF report, analysis/code files, and the complete application code.

## 1. Scope the project

- [ ] Write a one-paragraph problem definition for the report: the problem, intended users, classification objective, and practical value.
- [ ] Define the target labels precisely. For example, if labels are derived from star ratings, document the mapping and explain how neutral ratings are handled.
- [ ] Define success criteria: reproducible preprocessing, three fairly compared models, a justified selected model, a working app/API, and clear ethical analysis.
- [ ] Keep a short decision log in `docs/decision-log.md` for decisions about dataset, labels, features, models, and scope.

## 2. Select and document a dataset

- [ ] Choose one public e-commerce review dataset with review text and sentiment labels or ratings from which labels can be transparently derived.
- [ ] Confirm that it has a verifiable publisher/source, an appropriate licence or terms, enough rows for train/test evaluation, and genuine data-quality issues that require preparation.
- [ ] Do **not** use synthetic data.
- [ ] Use a static approved dataset rather than unauthorised live scraping.
- [ ] Create `docs/dataset-card.md` containing dataset name, publisher, licence, original URL, access date, size, fields, target definition, known limitations, and intended use.
- [ ] Record both the original-data URL and processed-data URL/instructions for the submission.
- [ ] Do not commit restricted or oversized raw data. Add it to `.gitignore` when necessary, while keeping a permitted sample/data dictionary and reproducible download instructions.

## 3. Set up a reproducible repository

- [ ] Create and pin a Python environment in `requirements.txt` or `pyproject.toml`.
- [ ] Use Git/GitHub with small, meaningful commits.
- [ ] Create the project structure:

```text
data/raw/              # ignored or link-only if restricted
data/processed/
docs/
notebooks/
src/data/
src/features/
src/models/
src/api/
app/
tests/
reports/figures/
reports/tables/
```

- [ ] Add a `.gitignore`, setup instructions, and a run guide.
- [ ] Fix random seeds where appropriate and record package versions.
- [ ] Use notebooks for exploration only; move repeatable production logic into `src/`.

## 4. Understand and prepare the data

- [ ] Load the original dataset and profile it: shape, column names, data types, descriptive statistics, missing/blank values, duplicates, class balance, text length, and obvious data errors.
- [ ] Produce and save basic data-understanding visualisations:
  - sentiment class counts;
  - review-length distribution by sentiment;
  - rating distribution, if ratings exist;
  - common words/n-grams, clearly labelled as exploratory.
- [ ] Define and justify cleaning rules. These should address:
  - missing or empty review text;
  - exact duplicate reviews/rows;
  - irrelevant identifiers and target-leakage attributes;
  - inconsistent text, whitespace, HTML, URLs, repeated punctuation, or malformed values;
  - the audit count of rows changed/removed at each step.
- [ ] Make the preprocessing reproducible with a script or pipeline, then save/document the processed-data output or a permissible link to it.
- [ ] Split into stratified train and held-out test sets before fitting learned transformations.
- [ ] Build all learned preprocessing inside scikit-learn pipelines, fitted only on training folds, to prevent data leakage.
- [ ] Use TF-IDF text features as the main representation; experiment with justified word/character n-grams and `min_df`/`max_df` settings.
- [ ] If retaining numerical or categorical features, encode categorical values and standardise/normalise numerical values where the model requires it. Explain every retained feature.

## 5. Implement three supervised models

Use three appropriate but distinct classifiers:

- [ ] **Multinomial Naive Bayes** - fast probabilistic text-classification baseline.
- [ ] **Logistic Regression** - linear discriminative model with interpretable feature weights.
- [ ] **Linear SVC** - margin-based linear model that is often strong for sparse TF-IDF text.
- [ ] For each model, document its principle, assumptions, strengths, limitations, suitability for this task, complete preprocessing pipeline, and parameter-search space.
- [ ] Keep every experiment and result in a consistent table; do not choose a model based on one favourable run.

## 6. Tune, validate, and evaluate

- [ ] Choose the primary metric before examining final test performance. Macro F1-score is a suitable primary metric if classes are imbalanced; explain the choice.
- [ ] Use stratified k-fold cross-validation (for example, 5 folds) on the training set for every candidate model.
- [ ] Tune parameters with `GridSearchCV` or `RandomizedSearchCV`:
  - Naive Bayes: `alpha`;
  - Logistic Regression: `C`, compatible penalty/solver, and class weights;
  - Linear SVC: `C` and class weights.
- [ ] Report cross-validation mean and standard deviation for each tuned model.
- [ ] Evaluate each final tuned model once on the held-out test set. Report:
  - accuracy;
  - precision, recall, and F1-score (including per-class results);
  - confusion matrix;
  - ROC-AUC only when the implementation and binary/multiclass setup make it valid.
- [ ] Present all models in a single comparison table and chart.
- [ ] Analyse representative false positives and false negatives. Consider sarcasm, short/mixed reviews, domain language, label noise, and class imbalance.
- [ ] Discuss evidence of underfitting or overfitting by comparing training, cross-validation, and test results.
- [ ] Run one or two planned robustness checks, such as feature-count or n-gram changes, and record the outcome.
- [ ] Select the model based on evidence and trade-offs, not only the highest score. Save the complete fitted pipeline and record its version/metrics.

## 7. Build the software application

The brief requires an input UI, results UI, workflow/business rules and authentication, and an API to the AI model.

- [ ] Use a manageable stack, for example Streamlit/React for the UI and FastAPI/Flask for the backend API.
- [ ] Include an architecture diagram:
  `User -> UI -> API -> validation/business rules -> model pipeline -> results/dashboard`.
- [ ] Implement an input screen with:
  - a sign-in flow or clearly bounded demonstration authentication;
  - review-text field and optional product/category field;
  - consent/privacy notice;
  - empty-text, length, and basic unsafe-input validation.
- [ ] Implement a results screen with:
  - predicted sentiment;
  - validly labelled confidence/probability or model score;
  - a limited explanation, such as influential terms, with its limitations;
  - accessible error messages.
- [ ] Implement a dashboard with sentiment counts/percentages, filters where supported by the data, trends, and examples. State that results are model predictions, not ground truth.
- [ ] Implement business rules:
  - reject empty or excessively long requests;
  - minimise storing user review text and require consent if storing it;
  - separate user-entered predictions from the original dataset;
  - never present predictions as factual judgements about customers.
- [ ] Provide and document API endpoints, such as `GET /health`, `POST /predict`, and `GET /dashboard/summary`.
- [ ] Define request/response schemas and meaningful errors.
- [ ] Add automated tests for preprocessing, invalid input, prediction response shape, and at least one successful API request.
- [ ] Record manual user-journey tests and results in `docs/test-plan.md`.

## 8. Complete the ethical analysis

- [ ] Discuss dataset bias: language, product category, demographics, culture, rating practices, class imbalance, and historical bias.
- [ ] Discuss performance limitations: mixed sentiment, sarcasm, minority dialects, and false positive/negative impact.
- [ ] Discuss privacy, possible personal data in reviews, and data minimisation/retention.
- [ ] Explain transparency: purpose, metrics, limitations, clear UI communication, and no overstated confidence.
- [ ] Explain accountability: humans review consequential decisions; this system is decision support only.
- [ ] Discuss provenance/licensing, reproducibility, security of stored text, and interface accessibility.
- [ ] Identify practical mitigations actually implemented.
- [ ] Declare and cite every use of AI assistance truthfully, in line with current university policy.

## 9. Write the PDF report

Do not invent results: each assertion must be supported by work and evidence from this project.

- [ ] **Introduction (one paragraph):** theme, problem, intended user, and classification task.
- [ ] **Experimental setup:** dataset source/size/features/limitations; preprocessing; algorithms and justification; parameter settings; cross-validation; metrics and rationale; app interface/architecture.
- [ ] **Results and visualisations:** data-understanding figures, model-performance table, confusion matrices/error plots, tuned results, and observed patterns.
- [ ] **Comparative analysis:** selected model and why; trade-offs; evidence of under/overfitting; error analysis and limitations.
- [ ] **Ethical analysis:** the project-specific risks and mitigations above.
- [ ] **Reflection:** learning from model development plus challenges in modelling/evaluation.
- [ ] **References:** datasets, sources, documentation, libraries, and other material used.
- [ ] Proofread for a clear, logical structure. Give every figure/table a meaningful title, caption, and source where appropriate.

## 10. Verify, package, and submit

- [ ] Re-run the project from the README instructions in a clean environment where possible.
- [ ] Confirm code is clean/reproducible and the repository has no secrets, unwanted files, or improperly shared restricted data.
- [ ] Prepare the final ZIP containing:
  - the report PDF;
  - code files (`.ipynb` and/or `.py`);
  - complete application code;
  - dependency/setup instructions;
  - original and processed dataset links;
  - any permitted data required to reproduce results.
- [ ] Open the ZIP and check the files before submitting it to Moodle.

## Suggested milestone order

1. Dataset selected, verified, and documented.
2. Exploratory analysis and cleaning pipeline complete.
3. Three baseline models and cross-validation running.
4. Tuning, comparisons, held-out evaluation, and error analysis complete.
5. API, input/results UI, dashboard, and authentication flow complete.
6. Tests, ethical analysis, report figures, and final PDF complete.
7. Reproducibility check, final ZIP check, and submission.

## Definition of done

The project is complete only when the dataset and preprocessing are documented and reproducible; all three models have been fairly tuned and compared with k-fold validation and suitable metrics; the selected model is connected through a tested API to a working application; the report critically evaluates results and ethics; and the final ZIP contains exactly the required deliverables.
