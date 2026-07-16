# Correlation Decision Logic

---

# Overview

This document describes how CLASSIFIC-AI evaluates relationships between numerical features and generates intelligent recommendations for handling correlated variables before machine learning.

Rather than automatically removing highly correlated features, the Correlation Decision Engine combines statistical evidence with business context to produce transparent and explainable recommendations.

Every recommendation requires human approval before implementation.

---

# Purpose

The objectives are to:

- Detect feature relationships
- Identify multicollinearity
- Reduce redundant information
- Improve model performance
- Support feature engineering
- Improve explainability
- Preserve business meaning
- Reduce model complexity

---

# Inputs

The Correlation Decision Engine consumes outputs from:

- Dataset Overview
- Column Intelligence
- Statistics Summary
- Correlation Analysis
- Feature Quality Assessment
- Business Rules

---

# Evaluation Dimensions

CLASSIFIC-AI evaluates:

- Pearson Correlation
- Spearman Correlation (Future)
- Kendall Correlation (Future)
- Correlation Matrix
- Correlation Heatmap
- Multicollinearity
- Business Importance
- Feature Redundancy

---

# Decision Logic

The engine evaluates every correlated feature pair independently.

---

## Very Low Correlation

IF

|Correlation| < 0.30

↓

Weak Relationship

↓

No Action Required

---

## Moderate Correlation

IF

0.30 ≤ |Correlation| < 0.70

↓

Useful Relationship

↓

Retain Feature

---

## Strong Correlation

IF

0.70 ≤ |Correlation| < 0.90

↓

Review Feature Pair

↓

Consider Business Importance

---

## Very Strong Correlation

IF

|Correlation| ≥ 0.90

↓

Potential Redundancy

↓

Recommend Feature Review

↓

Possible Removal

---

## Perfect Correlation

IF

|Correlation| = 1.00

↓

Duplicate Information

↓

Recommend Removing One Feature

---

## Multicollinearity

IF

Multiple Features Highly Correlated

↓

Recommend Multicollinearity Investigation

↓

Future Support

Variance Inflation Factor (VIF)

---

## Business Critical Features

IF

Highly Correlated Feature

AND

Business Critical

↓

Retain Feature

↓

Exclude Automatic Removal

---

# Correlation Categories

| Correlation | Interpretation | Recommendation |
|-------------|---------------|----------------|
| 0.00–0.29 | Weak | Keep |
| 0.30–0.69 | Moderate | Keep |
| 0.70–0.89 | Strong | Review |
| 0.90–0.99 | Very Strong | Investigate |
| 1.00 | Perfect | Remove Duplicate Feature |

---

# Recommendation Priority

Priority 1

Critical

- Perfect Correlation
- Duplicate Variables

---

Priority 2

High

- Very High Correlation
- Multicollinearity

---

Priority 3

Medium

- Strong Correlation

---

Priority 4

Low

- Moderate Correlation

---

# Business Decision Logic

Statistical correlation alone is not sufficient.

Business importance is always evaluated.

Example

Healthcare

Weight

BMI

↓

Highly Correlated

↓

Retain Both

↓

Medical Importance

---

Finance

Loan Amount

Outstanding Balance

↓

High Correlation

↓

Retain if Different Business Meaning

---

Retail

Sales Value

Revenue

↓

Perfect Correlation

↓

Retain One Variable

---

Manufacturing

Temperature (°C)

Temperature (°F)

↓

Perfect Correlation

↓

Keep One Standard Unit

---

# Human Approval

Correlation recommendations are never applied automatically.

Users may:

- Accept recommendations

- Reject recommendations

- Preserve business-critical variables

- Override thresholds

- Apply custom business rules

---

# Explainability

Every recommendation includes:

- Correlation Coefficient

- Correlation Strength

- Statistical Evidence

- Business Interpretation

- Confidence Level

- Recommended Action

- Expected Model Impact

This ensures every decision made by CLASSIFIC-AI is transparent and explainable.

---

# Future Enhancements

Version 2.0

Future improvements include:

- Variance Inflation Factor (VIF)

- Partial Correlation

- Mutual Information

- Nonlinear Correlation Detection

- Automatic Redundancy Detection

- AI-powered Feature Dependency Analysis

---

# Interaction with Other Modules

This decision engine supports:

- Preprocessing Agent

- Business Rules Agent

- Feature Engineering Agent

- Feature Selection Agent

- Model Recommendation Agent

- Explainability Agent

- RAG Agent

- AI Copilot

The recommendations generated here guide feature engineering, feature selection, dimensionality reduction, and model optimization throughout the CLASSIFIC-AI pipeline.

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
