# Missing Value Recommendations

---

# Overview

This document describes how CLASSIFIC-AI recommends appropriate strategies for handling missing values detected during the Data Profiling stage.

Rather than recommending a single universal solution, CLASSIFIC-AI evaluates the percentage of missing values, feature characteristics, business importance, and machine learning compatibility before generating recommendations.

The objective is to preserve valuable information while minimizing the impact of incomplete data on downstream analytics and machine learning models.

---

# Purpose

The objectives are to:

- Identify missing value severity
- Recommend appropriate imputation techniques
- Reduce information loss
- Improve model performance
- Preserve business meaning
- Support explainable AI
- Assist preprocessing decisions

---

# Recommendation Factors

CLASSIFIC-AI evaluates:

- Missing Percentage
- Feature Type
- Data Type
- Business Importance
- Distribution
- Cardinality
- Target Variable Availability
- Machine Learning Compatibility

---

# Recommendation Rules

## No Missing Values

Condition

Missing Percentage = 0%

Recommendation

✓ No Action Required

---

## Very Low Missing Values

Condition

Missing Percentage <5%

Recommendation

- Mean Imputation
- Median Imputation
- Mode Imputation

Depending on feature type.

---

## Low Missing Values

Condition

5–15%

Recommendation

- Statistical Imputation

- KNN Imputation (Future)

- Business Review

---

## Moderate Missing Values

Condition

15–30%

Recommendation

- Advanced Imputation

- Business Validation

- Evaluate Feature Importance

---

## High Missing Values

Condition

30–50%

Recommendation

Human Review

Possible options

- Remove Feature

- Retain if Business Critical

- Advanced Imputation

---

## Very High Missing Values

Condition

>50%

Recommendation

Strongly Recommend Feature Removal

unless business critical.

---

# Recommendations by Data Type

## Numerical Features

Recommended Techniques

- Mean
- Median
- Regression Imputation (Future)
- KNN Imputation (Future)

---

## Categorical Features

Recommended Techniques

- Mode
- Unknown Category
- Business Category

---

## Date Features

Recommended Techniques

- Previous Date
- Next Date
- Business Rule

---

## Text Features

Recommended Techniques

- Empty String

- Unknown

- NLP Processing

---

# Business Examples

## Healthcare

Blood Pressure

↓

5% Missing

↓

Median Imputation

---

## Finance

Annual Income

↓

40% Missing

↓

Business Review

↓

Possible Removal

---

## Retail

Customer Segment

↓

Missing

↓

Unknown Category

---

## Manufacturing

Sensor Reading

↓

Missing

↓

Investigate Equipment

---

# Human Approval

Recommendations are never applied automatically.

Users may:

- Accept recommendation

- Reject recommendation

- Override thresholds

- Apply business-specific rules

---

# Explainability

Every recommendation includes:

- Missing Percentage

- Feature Type

- Statistical Evidence

- Business Impact

- Recommended Technique

- Expected Model Impact

---

# Future Enhancements

Version 2.0

Future improvements include:

- AI Imputation Recommendation

- Multiple Imputation

- Deep Learning Imputation

- Simulation-based Evaluation

- Industry-specific Rules

---

# Interaction with Other Modules

Supports:

- Preprocessing Agent

- Business Rules Agent

- Feature Engineering Agent

- Model Recommendation Agent

- Simulation Agent

- RAG Agent

- AI Copilot

---

# Version

Current Version: **1.0**

Planned Version: **2.0**

---

# Author

**Biswadip Choudhury**

---

# Project

**CLASSIFIC-AI**

**Open Source Intelligent Machine Learning Framework**
