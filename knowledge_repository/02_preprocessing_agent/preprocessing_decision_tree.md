# Preprocessing Decision Tree

---

# Overview

The Preprocessing Decision Tree describes the intelligent decision-making process used by the CLASSIFIC-AI Preprocessing Agent.

Instead of applying preprocessing blindly, CLASSIFIC-AI evaluates the characteristics of each feature and recommends the most appropriate preprocessing technique.

Every recommendation follows a transparent, explainable, and Human-in-the-Loop (HITL) approach.

---

# Purpose

The objectives of the Preprocessing Decision Tree are:

- Explain recommendation logic
- Standardize preprocessing decisions
- Improve explainability
- Reduce preprocessing errors
- Support Human-in-the-Loop
- Improve downstream model performance

---

# Master Decision Flow

```

Dataset

│

▼

Analyze Feature

│

├───────────────┐

▼ ▼

Numerical Categorical

│ │

▼ ▼

Outliers? Cardinality?

│ │

▼ ▼

Scaling Encoding

│ │

▼ ▼

Recommendation Recommendation

│

▼

Human Approval

│

▼

Next Agent

```

---

# Decision Tree 1

## Duplicate Detection

```

Duplicate Rows?

│

├──── No

│

▼

Continue

│

└──── Yes

│

▼

Calculate Duplicate Percentage

│

├──── < 5%

│

▼

Review

│

└──── ≥ 5%

│

▼

Recommend Removal

│

▼

Human Approval

```

---

# Decision Tree 2

## Missing Value Detection

```

Missing Values?

│

├──── No

│

▼

Continue

│

└──── Yes

│

▼

Column Type?

│

├──────────────┐

▼ ▼

Numerical Categorical

│ │

▼ ▼

Median Mode

Mean Unknown

KNN Business Rule

│

▼

Human Approval

```

---

# Decision Tree 3

## Data Type Detection

```

Column

│

▼

Detect Data Type

│

├──────────────┬─────────────┬──────────────┬─────────────┬─────────────┐

▼ ▼ ▼ ▼ ▼

Numeric Category Date Text Boolean

│ │ │ │ │

▼ ▼ ▼ ▼ ▼

Scaling Encoding Feature TF-IDF Binary

Extraction Embeddings Conversion

```

---

# Decision Tree 4

## Outlier Detection

```

Numerical Feature

│

▼

Outliers?

│

├──── No

│

▼

Continue

│

└──── Yes

│

▼

Business Important?

│

├──── Yes

│

▼

Keep

RobustScaler

│

└──── No

│

▼

Review

Remove

Winsorize

Transform

```

---

# Decision Tree 5

## Encoding Recommendation

```

Categorical Feature

│

▼

Cardinality

│

├────────────┬───────────────┬─────────────────┐

▼ ▼ ▼

Low Medium High

│ │ │

▼ ▼ ▼

One-Hot Frequency Embeddings

Encoding Encoding Target Encoding

```

---

# Decision Tree 6

## Scaling Recommendation

```

Numerical Feature

│

▼

Distribution

│

├──────────────┬───────────────┬──────────────┐

▼ ▼ ▼

Normal Outliers Fixed Range

│ │ │

▼ ▼ ▼

Standard Robust MinMax

Scaler Scaler Scaler

```

---

# Decision Tree 7

## Date Detection

```

Date Feature

│

▼

Extract Components

│

├────────────┬──────────────┬──────────────┐

▼ ▼ ▼

Year Month Quarter

│

▼

Business Features

Holiday

Weekend

Fiscal Quarter

```

---

# Decision Tree 8

## Text Detection

```

Text Feature

│

▼

Average Length

│

├──────────────┬───────────────┬────────────────┐

▼ ▼ ▼

Short Medium Long

│ │ │

▼ ▼ ▼

Encoding TF-IDF Embeddings

Transformer

```

---

# Decision Tree 9

## Boolean Detection

```

Two Unique Values?

│

├──── No

│

▼

Treat as Category

│

└──── Yes

│

▼

Boolean Feature

│

▼

Convert to Binary

│

▼

Human Approval

```

---

# Decision Tree 10

## Constant Feature Detection

```

Unique Values

│

▼

Only One?

│

├──── No

│

▼

Keep Feature

│

└──── Yes

│

▼

Recommend Removal

│

▼

Human Approval

```

---

# Decision Tree 11

## High Cardinality Detection

```

Unique Percentage

│

├─────────────┬─────────────┬──────────────┐

▼ ▼ ▼

Low Medium High

│ │ │

▼ ▼ ▼

One-Hot Frequency Embeddings

Encoding Encoding

```

---

# Decision Tree 12

## ID Detection

```

Identifier?

│

├──── No

│

▼

Continue

│

└──── Yes

│

▼

Business Identifier?

│

├──── Yes

│

▼

Keep

Exclude from Model

│

└──── No

│

▼

Exclude

```

---

# Recommendation Engine

```

All Recommendations

│

▼

Merge Results

│

▼

Dataset Health Score

│

▼

Generate Report

│

▼

Human Approval

│

▼

Data Profiling Agent

```

---

# Human-in-the-Loop

Every decision generated by the Preprocessing Decision Tree requires user review before execution.

The user may:

- Accept recommendation
- Modify recommendation
- Reject recommendation
- Apply business rules
- Save preprocessing strategy

---

# Benefits

The Decision Tree provides:

- Explainable AI
- Transparent preprocessing
- Standardized recommendations
- Reproducible preprocessing
- Reduced human error
- Improved governance

---

# Future Enhancements

Version 2.0

Planned improvements:

- AI-generated decision trees
- Dynamic recommendation paths
- Domain-specific decision trees
- Probability-based recommendations
- Confidence scoring
- Learning from user feedback

---

# Related Knowledge Assets

- preprocessing_workflow.md
- recommendation_engine.md
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
