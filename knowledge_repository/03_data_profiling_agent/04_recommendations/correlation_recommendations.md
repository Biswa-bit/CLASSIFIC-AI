# Correlation Recommendations

---

# Overview

This document describes how CLASSIFIC-AI recommends actions after analyzing correlations between numerical features.

Highly correlated variables may introduce redundancy, reduce model interpretability, and increase multicollinearity in certain machine learning algorithms. CLASSIFIC-AI evaluates correlation strength together with business context before generating recommendations.

The objective is to reduce redundant information while preserving valuable business knowledge.

---

# Purpose

The objectives are to:

- Detect highly correlated features
- Reduce redundant information
- Improve model interpretability
- Minimize multicollinearity
- Preserve business-critical variables
- Support explainable AI
- Assist feature selection decisions

---

# Recommendation Factors

CLASSIFIC-AI evaluates:

- Correlation Coefficient
- Correlation Direction
- Feature Importance
- Business Importance
- Target Relationship
- Multicollinearity Risk
- Machine Learning Algorithm
- Feature Redundancy

---

# Recommendation Rules

## Very Weak Correlation

Condition

|Correlation| < 0.30

Recommendation

✓ No Action Required

↓

Retain Both Features

---

## Moderate Correlation

Condition

0.30 ≤ |Correlation| < 0.70

Recommendation

Monitor Relationship

↓

Business Review

↓

Retain Features

---

## Strong Correlation

Condition

0.70 ≤ |Correlation| < 0.90

Recommendation

Review Features

↓

Evaluate Feature Importance

↓

Possible Feature Reduction

---

## Very Strong Correlation

Condition

|Correlation| ≥ 0.90

Recommendation

Investigate Redundancy

↓

Retain Most Informative Feature

↓

Business Validation Required

---

## Perfect Correlation

Condition

|Correlation| = 1.00

Recommendation

Remove Duplicate Feature

unless required for business reporting.

---

# Recommendations by Algorithm

## Linear Regression

Recommendation

Remove highly correlated variables.

Perform VIF analysis before modeling.

---

## Logistic Regression

Recommendation

Reduce multicollinearity when necessary.

Validate using VIF.

---

## Decision Tree

Recommendation

Usually safe.

Feature removal optional.

---

## Random Forest

Recommendation

Generally tolerant of correlated features.

Feature reduction may improve interpretability.

---

## Gradient Boosting

Recommendation

Review correlated variables.

Feature pruning may improve efficiency.

---

## XGBoost

Recommendation

Correlation rarely causes performance issues.

Feature importance should guide removal.

---

## Neural Networks

Recommendation

Feature reduction is optional.

Normalize inputs when required.

---

# Correlation Threshold Guide

| Absolute Correlation | Recommendation |
|----------------------|----------------|
| < 0.30 | No Action |
| 0.30 – 0.70 | Review |
| 0.70 – 0.90 | Consider Reduction |
| ≥ 0.90 | Strong Recommendation to Review |
| 1.00 | Remove Duplicate Feature |

---

# Business Examples

## Healthcare

Height

Weight

↓

Moderately Correlated

↓

Retain Both

Both provide independent clinical value.

---

## Finance

Annual Income

Monthly Income

↓

Perfect Correlation

↓

Keep One Variable

---

## Retail

Sales

Revenue

↓

Highly Correlated

↓

Business Review

↓

Select Most Informative Feature

---

## Manufacturing

Temperature Sensor A

Temperature Sensor B

↓

Very High Correlation

↓

Check Sensor Duplication

---

# Human Approval

Correlation recommendations are never applied automatically.

Users may:

- Accept recommendations

- Reject recommendations

- Keep all variables

- Remove selected features

- Apply business-specific rules

---

# Explainability

Each recommendation includes:

- Correlation Value

- Correlation Strength

- Statistical Evidence

- Business Importance

- Suggested Action

- Expected Model Impact

- Algorithm Considerations

---

# Future Enhancements

Version 2.0

Future improvements include:

- Automatic Feature Clustering

- AI-based Redundancy Detection

- Correlation Network Analysis

- Target-aware Correlation Analysis

- Graph-based Feature Relationships

- Industry-specific Correlation Rules

---

# Interaction with Other Modules

Supports:

- Feature Engineering Agent

- Feature Selection Agent

- Model Recommendation Agent

- Hyperparameter Optimization Agent

- Explainability Agent

- RAG Agent

- AI Copilot

The recommendations generated here help optimize feature selection, improve model interpretability, and reduce unnecessary feature redundancy throughout the CLASSIFIC-AI pipeline.

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
