# Distribution Decision Logic

---

# Overview

This document describes how CLASSIFIC-AI evaluates the statistical distribution of numerical features and generates intelligent recommendations before preprocessing and machine learning.

Rather than assuming every numerical feature follows a normal distribution, the Distribution Decision Engine analyzes multiple statistical indicators to determine the most appropriate preprocessing strategy.

Every recommendation is transparent, explainable, and requires human approval before implementation.

---

# Purpose

The objectives are to:

- Evaluate feature distributions
- Detect non-normal data
- Recommend suitable preprocessing techniques
- Improve model performance
- Reduce statistical bias
- Support explainable AI
- Assist feature engineering
- Improve downstream model selection

---

# Inputs

The Distribution Decision Engine consumes outputs from:

- Dataset Overview
- Statistics Summary
- Distribution Analysis
- Normality Tests
- Skewness Analysis
- Kurtosis Analysis
- Outlier Detection

---

# Evaluation Dimensions

CLASSIFIC-AI evaluates numerical features using:

- Mean
- Median
- Standard Deviation
- Variance
- Skewness
- Kurtosis
- Histogram Shape
- Normality Test Results
- Outlier Presence

---

# Decision Logic

The engine evaluates every numerical feature independently.

---

## Normally Distributed Feature

IF

Normality Test

=

Pass

AND

|Skewness| < 0.5

↓

Feature is Approximately Normal

↓

No Transformation Required

---

## Moderately Skewed Feature

IF

0.5 ≤ |Skewness| < 1.0

↓

Recommend Review

↓

Consider Transformation if Required

---

## Highly Skewed Feature

IF

|Skewness| ≥ 1.0

↓

Recommend Transformation

Possible Techniques

- Log Transformation
- Square Root Transformation
- Box-Cox Transformation
- Yeo-Johnson Transformation

---

## Heavy-Tailed Distribution

IF

Kurtosis > 3

↓

Potential Extreme Values

↓

Investigate Outliers

↓

Recommend RobustScaler if Appropriate

---

## Light-Tailed Distribution

IF

Kurtosis < 3

↓

Distribution Less Sensitive to Outliers

↓

Proceed with Standard Analysis

---

## Presence of Outliers

IF

Consensus Outlier Detection

=

High

↓

Recommend Outlier Investigation

↓

Distribution Interpretation Requires Caution

---

## Multiple Peaks

IF

Distribution is Multimodal

↓

Investigate Data Segmentation

↓

Review Business Context

---

# Distribution Categories

| Observation | Recommendation |
|-------------|----------------|
| Approximately Normal | No Transformation Required |
| Moderately Skewed | Review Transformation |
| Highly Skewed | Apply Suitable Transformation |
| Heavy-Tailed | Investigate Outliers |
| Multimodal | Review Population Segments |
| Unknown Pattern | Human Review Required |

---

# Recommendation Priority

Priority 1

Critical

- Invalid Numerical Values
- Corrupted Distribution
- Extreme Skewness

---

Priority 2

High

- Heavy Tails
- Severe Outliers
- Strong Non-Normality

---

Priority 3

Medium

- Moderate Skewness
- Mild Kurtosis

---

Priority 4

Low

- Minor Distribution Deviations

---

# Business Decision Logic

Statistical results are interpreted together with business context.

Example

Healthcare

Patient Age

↓

Right Skewed

↓

Keep Distribution

↓

No Transformation

Business Interpretation

Older patients are naturally fewer.

---

Finance

Annual Income

↓

Highly Right Skewed

↓

Recommend Log Transformation

---

Retail

Purchase Amount

↓

Heavy Tail

↓

Recommend RobustScaler

---

Manufacturing

Machine Vibration

↓

Multimodal

↓

Investigate Multiple Operating Modes

---

# Human Approval

Distribution-based recommendations are never applied automatically.

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

- Statistical Evidence

- Skewness

- Kurtosis

- Normality Result

- Business Interpretation

- Recommended Action

- Expected Model Impact

---

# Future Enhancements

Version 2.0

Future improvements include:

- AI Distribution Classification

- Automatic Transformation Selection

- Distribution Drift Detection

- Industry-specific Distribution Rules

- Time-Series Distribution Analysis

- Simulation-based Distribution Testing

---

# Interaction with Other Modules

This decision engine supports:

- Preprocessing Agent

- Business Rules Agent

- Feature Engineering Agent

- Feature Selection Agent

- Model Recommendation Agent

- Simulation Agent

- Explainability Agent

- RAG Agent

- AI Copilot

The recommendations generated here influence preprocessing, feature engineering, scaling, transformation, and model selection throughout the CLASSIFIC-AI pipeline.

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
