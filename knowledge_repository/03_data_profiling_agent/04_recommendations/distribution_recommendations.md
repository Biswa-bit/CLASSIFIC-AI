# Distribution Recommendations

---

# Overview

This document describes how CLASSIFIC-AI recommends appropriate actions after analyzing the statistical distribution of numerical features.

Rather than assuming all numerical variables should follow a normal distribution, CLASSIFIC-AI evaluates distribution characteristics together with business context before recommending preprocessing techniques.

The objective is to improve model performance while preserving meaningful business information.

---

# Purpose

The objectives are to:

- Evaluate feature distributions
- Recommend suitable transformations
- Improve statistical assumptions
- Enhance model performance
- Preserve business meaning
- Support explainable AI
- Assist preprocessing decisions

---

# Recommendation Factors

CLASSIFIC-AI evaluates:

- Distribution Shape
- Skewness
- Kurtosis
- Normality Test Results
- Outlier Presence
- Business Importance
- Feature Type
- Machine Learning Compatibility

---

# Recommendation Rules

## Approximately Normal Distribution

Condition

Normality Test Passed

AND

|Skewness| < 0.5

Recommendation

✓ No Transformation Required

↓

Proceed with Modeling

---

## Slightly Skewed Distribution

Condition

0.5 ≤ |Skewness| < 1.0

Recommendation

Review Feature

↓

Transformation Optional

↓

Business Validation

---

## Highly Skewed Distribution

Condition

|Skewness| ≥ 1.0

Recommendation

Consider:

- Log Transformation

- Square Root Transformation

- Box-Cox Transformation

- Yeo-Johnson Transformation

---

## Heavy-Tailed Distribution

Condition

Kurtosis > 3

Recommendation

Investigate Outliers

↓

Consider RobustScaler

↓

Review Distribution

---

## Light-Tailed Distribution

Condition

Kurtosis < 3

Recommendation

Proceed

↓

No Immediate Action Required

---

## Multimodal Distribution

Condition

Multiple Peaks

Recommendation

Investigate

↓

Possible Population Segmentation

↓

Business Review

---

## Uniform Distribution

Condition

Uniform Feature

Recommendation

Review Business Meaning

↓

No Automatic Transformation

---

# Recommendations by Distribution Type

| Distribution | Recommendation |
|--------------|----------------|
| Normal | No Transformation |
| Slightly Skewed | Review |
| Highly Skewed | Transformation Recommended |
| Heavy-Tailed | Investigate Outliers |
| Light-Tailed | Proceed |
| Uniform | Business Validation |
| Multimodal | Segment Analysis |

---

# Transformation Recommendations

## Log Transformation

Recommended For

- Income
- Revenue
- Sales
- Claim Amount
- Transaction Value

---

## Square Root Transformation

Recommended For

- Count Data
- Moderate Right Skew

---

## Box-Cox Transformation

Recommended For

- Positive Numerical Variables

---

## Yeo-Johnson Transformation

Recommended For

- Variables Containing Zero
- Variables Containing Negative Values

---

## RobustScaler

Recommended When

- Heavy Tails
- Extreme Outliers

---

## StandardScaler

Recommended When

- Approximately Normal Distribution

---

## MinMaxScaler

Recommended When

- Neural Networks

- Distance-Based Algorithms

- Known Numerical Range

---

# Business Examples

## Healthcare

Patient Age

↓

Slightly Right Skewed

↓

No Transformation

↓

Business Interpretation Preferred

---

## Finance

Annual Income

↓

Highly Right Skewed

↓

Log Transformation

---

## Retail

Purchase Amount

↓

Heavy Tail

↓

RobustScaler

---

## Manufacturing

Machine Runtime

↓

Multimodal

↓

Investigate Operating Modes

---

# Human Approval

Distribution recommendations are never applied automatically.

Users may:

- Accept recommendations

- Reject recommendations

- Override thresholds

- Preserve original distributions

- Apply business-specific preprocessing

---

# Explainability

Each recommendation includes:

- Distribution Type

- Skewness

- Kurtosis

- Normality Result

- Statistical Evidence

- Business Interpretation

- Recommended Action

- Expected Model Impact

---

# Future Enhancements

Version 2.0

Future improvements include:

- AI Transformation Recommendation

- Automatic Distribution Classification

- Distribution Drift Detection

- Time-Series Distribution Analysis

- Simulation-based Transformation Testing

- Industry-specific Distribution Rules

---

# Interaction with Other Modules

Supports:

- Preprocessing Agent

- Business Rules Agent

- Feature Engineering Agent

- Model Recommendation Agent

- Simulation Agent

- Explainability Agent

- RAG Agent

- AI Copilot

The recommendations generated here guide preprocessing, scaling, transformation, feature engineering, and model optimization throughout the CLASSIFIC-AI pipeline.

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
