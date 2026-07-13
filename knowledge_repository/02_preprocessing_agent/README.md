# CLASSIFIC-AI Knowledge Repository

# Preprocessing Agent

---

## Overview

The Preprocessing Agent is the second intelligent agent in the CLASSIFIC-AI framework.

Its responsibility is to automatically analyze the uploaded dataset, detect data quality issues, recommend appropriate preprocessing techniques, and prepare the dataset for downstream statistical analysis and machine learning.

Unlike traditional preprocessing pipelines that immediately modify data, the CLASSIFIC-AI Preprocessing Agent follows a recommendation-first approach. Every recommendation is presented to the user for review before execution, ensuring human oversight for business-critical decisions.

---

## Objectives

The objectives of the Preprocessing Agent are:

- Improve data quality
- Detect common data issues
- Reduce manual preprocessing effort
- Recommend appropriate preprocessing techniques
- Prevent incorrect preprocessing decisions
- Prepare data for Data Profiling Agent
- Support Human-in-the-Loop governance

---

## Position in CLASSIFIC-AI Pipeline

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

The output of the Preprocessing Agent becomes the input for the Data Profiling Agent.

---

# Responsibilities

The Preprocessing Agent performs the following analyses.

| Module | Purpose |
|---------|----------|
| Duplicate Detection | Detect duplicate records |
| Missing Value Detection | Identify missing values |
| Data Type Detection | Detect incorrect data types |
| Outlier Detection | Identify statistical outliers |
| Encoding Recommendation | Recommend categorical encoding |
| Scaling Recommendation | Recommend feature scaling |
| Date Detection | Detect datetime columns |
| Text Detection | Detect NLP features |
| Boolean Detection | Detect True/False features |
| Constant Feature Detection | Detect zero-variance columns |
| High Cardinality Detection | Detect columns with many unique values |
| ID Detection | Detect identifier columns |
| Recommendation Engine | Generate preprocessing recommendations |

---

# Human-in-the-Loop Design

CLASSIFIC-AI never performs preprocessing automatically.

Instead, the Preprocessing Agent:

- analyzes the dataset
- generates recommendations
- explains the reasoning
- requests human approval before execution

This design prevents accidental data modification and preserves business context.

---

# Input

The Preprocessing Agent accepts:

- Pandas DataFrame
- CSV datasets
- Excel (.xlsx)
- Excel (.xls)
- Parquet
- JSON
- Feather
- Pickle

Additional formats will be supported in future releases.

---

# Output

The agent produces:

- Data quality summary
- Column-level analysis
- Detected issues
- Recommended preprocessing techniques
- Human approval recommendations
- Dataset readiness assessment

---

# Benefits

The Preprocessing Agent provides:

- Improved data quality
- Consistent preprocessing
- Reduced manual work
- Better model performance
- Improved explainability
- Standardized ML workflow

---

# Interaction with Other Agents

The Preprocessing Agent works closely with:

- Dataset Agent
- Data Profiling Agent
- Business Rules Agent
- Feature Engineering Agent
- Model Recommendation Agent

Its recommendations influence every downstream agent.

---

# Future Enhancements

Planned improvements include:

- Language detection
- Spell checking
- Text normalization
- Token statistics
- Stopword analysis
- Named Entity Recognition (NER)
- Embedding recommendation
- AI-powered preprocessing suggestions
- Automatic preprocessing pipeline generation

---

# Related Documentation

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

Project: CLASSIFIC-AI

Open Source Intelligent Machine Learning Framework
