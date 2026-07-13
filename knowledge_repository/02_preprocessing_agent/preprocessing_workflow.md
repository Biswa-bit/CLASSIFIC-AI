# Preprocessing Workflow

---

# Overview

The Preprocessing Workflow defines the sequence of operations performed by the CLASSIFIC-AI Preprocessing Agent.

Rather than applying preprocessing techniques immediately, the workflow first analyzes the dataset, identifies potential data quality issues, generates intelligent recommendations, and presents them to the user for approval.

This recommendation-first approach ensures that preprocessing decisions remain transparent, explainable, and aligned with business objectives.

---

# Objectives

The objectives of the preprocessing workflow are:

- Improve data quality
- Detect data quality issues
- Generate preprocessing recommendations
- Preserve business information
- Support Human-in-the-Loop (HITL)
- Prepare data for statistical profiling
- Improve downstream machine learning performance

---

# Position in CLASSIFIC-AI Pipeline

```
Dataset Agent
        │
        ▼
Preprocessing Agent
        │
        ▼
Data Profiling Agent
        │
        ▼
EDA Agent
        │
        ▼
Business Rules Agent
        │
        ▼
Feature Engineering Agent
        │
        ▼
Feature Selection Agent
        │
        ▼
Model Recommendation Agent
```

---

# Complete Workflow

```
Dataset Uploaded

        │

        ▼

Dataset Validation

        │

        ▼

Duplicate Detection

        │

        ▼

Missing Value Detection

        │

        ▼

Data Type Detection

        │

        ▼

Outlier Detection

        │

        ▼

Encoding Recommendation

        │

        ▼

Scaling Recommendation

        │

        ▼

Date Detection

        │

        ▼

Text Detection

        │

        ▼

Boolean Detection

        │

        ▼

Constant Feature Detection

        │

        ▼

High Cardinality Detection

        │

        ▼

ID Detection

        │

        ▼

Recommendation Engine

        │

        ▼

Human Approval

        │

        ▼

Data Profiling Agent
```

---

# Why This Order?

Every preprocessing step depends on the results of previous analyses.

For example:

- Duplicate detection should occur before statistical analysis.
- Missing values should be identified before feature engineering.
- Data types should be validated before encoding.
- Outliers should be reviewed before feature scaling.
- High-cardinality detection should occur before encoding recommendations.

This sequence minimizes preprocessing errors and improves recommendation quality.

---

# Workflow Explanation

## Step 1 — Duplicate Detection

Purpose

Identify duplicate observations that may bias statistical analysis and model training.

Output

- Duplicate Count
- Duplicate Percentage
- Recommendation

---

## Step 2 — Missing Value Detection

Purpose

Identify incomplete observations and recommend suitable handling strategies.

Output

- Missing Count
- Missing Percentage
- Imputation Recommendation

---

## Step 3 — Data Type Detection

Purpose

Identify numerical, categorical, boolean, text, date, and identifier features.

Output

- Feature Type
- Recommended Processing

---

## Step 4 — Outlier Detection

Purpose

Detect extreme numerical observations.

Output

- Outlier Count
- Detection Method
- Recommendation

---

## Step 5 — Encoding Recommendation

Purpose

Recommend suitable encoding techniques for categorical variables.

Output

- One-Hot Encoding
- Frequency Encoding
- Embeddings
- Other Recommendations

---

## Step 6 — Scaling Recommendation

Purpose

Recommend suitable scaling techniques for numerical features.

Output

- StandardScaler
- RobustScaler
- MinMaxScaler

---

## Step 7 — Date Detection

Purpose

Detect temporal features and recommend feature extraction.

Output

- Calendar Features
- Business Date Features

---

## Step 8 — Text Detection

Purpose

Identify text columns requiring NLP preprocessing.

Output

- TF-IDF
- Embeddings
- NLP Recommendation

---

## Step 9 — Boolean Detection

Purpose

Identify logical variables and recommend binary conversion.

Output

- Boolean Mapping
- Binary Recommendation

---

## Step 10 — Constant Feature Detection

Purpose

Identify zero-variance features.

Output

- Constant Columns
- Removal Recommendation

---

## Step 11 — High Cardinality Detection

Purpose

Detect categorical variables with many unique values.

Output

- Cardinality Percentage
- Encoding Recommendation

---

## Step 12 — ID Detection

Purpose

Identify identifier columns.

Output

- Identifier Detection
- Exclusion Recommendation

---

## Step 13 — Recommendation Engine

Purpose

Combine all preprocessing results into a unified recommendation report.

Output

- Dataset Health Score
- Column Recommendations
- Human Approval Report

---

# Human-in-the-Loop

CLASSIFIC-AI follows a Human-in-the-Loop (HITL) architecture.

Instead of automatically modifying datasets, every recommendation is presented to the user for review.

The user can:

- Accept all recommendations
- Accept selected recommendations
- Modify recommendations
- Reject recommendations
- Apply custom business rules

---

# Benefits

The preprocessing workflow provides:

- Improved data quality
- Transparent preprocessing
- Explainable recommendations
- Better model performance
- Reduced preprocessing errors
- Business-aware decision making

---

# Future Workflow

Version 2.0 will introduce:

- AI-generated preprocessing pipelines
- Adaptive workflow optimization
- Automatic preprocessing templates
- Domain-specific preprocessing
- Confidence scoring
- Workflow learning from user feedback

---

# Related Knowledge Assets

- README.md
- duplicate_detection.md
- missing_value_detection.md
- datatype_detection.md
- outlier_detection.md
- encoding_recommendation.md
- scaling_recommendation.md
- date_detection.md
- text_detection.md
- boolean_detection.md
- constant_feature_detection.md
- high_cardinality_detection.md
- id_detection.md
- recommendation_engine.md

---

# Version

Current Version: 1.0

Planned Version: 2.0

---

# Author

Biswadip Choudhury

Project

CLASSIFIC-AI

Open Source Intelligent Machine Learning Framework
