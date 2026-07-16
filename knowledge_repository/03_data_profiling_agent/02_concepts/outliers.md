# Outliers

---

# Overview

Outliers are observations that differ significantly from the majority of the data.

They may represent:

- Data entry errors
- Measurement errors
- Rare events
- Fraudulent transactions
- Exceptional business cases
- Natural variation

Within CLASSIFIC-AI, Outlier Detection is treated as an explainable decision-making process rather than an automatic data cleaning step.

The system evaluates multiple statistical methods before generating recommendations and always requires human approval before removing observations.

---

# Definition

An outlier is an observation whose value lies far away from the majority of observations within the same feature.

Outliers may be:

- Global Outliers
- Contextual Outliers
- Collective Outliers

Not every outlier is incorrect.

Many outliers contain valuable business information.

---

# Objectives

The objectives of Outlier Analysis are:

- Detect unusual observations
- Improve data quality
- Support preprocessing decisions
- Reduce model bias
- Improve model performance
- Detect business anomalies
- Support explainable AI

---

# Why Outlier Detection is Important

Outliers may significantly influence:

- Mean
- Standard Deviation
- Regression Models
- Distance-Based Algorithms
- Clustering Algorithms

However, removing every outlier is not always appropriate.

Examples include:

Healthcare

Rare disease patients

Finance

Fraudulent transactions

Retail

VIP customers

Manufacturing

Machine failures

These observations often provide valuable business insights.

---

# Types of Outliers

## Global Outliers

Observations that differ substantially from the entire dataset.

Example

Salary

250000

when most salaries range between

30000–80000

---

## Contextual Outliers

Values that appear normal in one context but abnormal in another.

Example

Temperature

40°C

Normal in summer

Abnormal in winter

---

## Collective Outliers

A group of observations that together form an unusual pattern.

Common in:

- Time Series
- IoT
- Sensor Data

---

# Outlier Detection Methods

CLASSIFIC-AI currently supports:

- Interquartile Range (IQR)
- Z-Score
- Modified Z-Score
- Consensus Detection

Future versions will include:

- Isolation Forest
- Local Outlier Factor (LOF)
- DBSCAN
- One-Class SVM
- Elliptic Envelope

---

# Interquartile Range (IQR)

The IQR method detects observations outside the expected range.

Formula

IQR = Q3 − Q1

Lower Bound

Q1 − 1.5 × IQR

Upper Bound

Q3 + 1.5 × IQR

Observations outside these limits are considered potential outliers.

---

# Z-Score

The Z-Score measures how many standard deviations an observation is from the mean.

Formula

Z = (X − Mean) / Standard Deviation

Typical Threshold

|Z| > 3

Best suited for approximately normal distributions.

---

# Modified Z-Score

The Modified Z-Score is a robust alternative that uses the Median Absolute Deviation (MAD).

Formula

Modified Z = 0.6745 × (X − Median) / MAD

Typical Threshold

|Modified Z| > 3.5

Recommended for skewed datasets because it is less sensitive to extreme values.

---

# Consensus Outlier Detection

One of the distinguishing features of CLASSIFIC-AI is Consensus Outlier Detection.

Instead of relying on a single statistical method, the framework compares:

- IQR
- Z-Score
- Modified Z-Score

The final recommendation is based on agreement among multiple methods, increasing reliability and reducing false positives.

---

# Outlier Severity Levels

CLASSIFIC-AI classifies outlier severity based on the proportion of detected outliers.

| Outlier Percentage | Severity |
|-------------------|----------|
| <1% | Very Low |
| 1–5% | Low |
| 5–10% | Moderate |
| 10–20% | High |
| >20% | Very High |

Severity helps prioritize investigation and preprocessing.

---

# CLASSIFIC-AI Decision Logic

| Observation | Recommendation |
|-------------|----------------|
| Very Low Severity | No Action Required |
| Low Severity | Monitor Feature |
| Moderate Severity | Business Review Recommended |
| High Severity | Human Investigation Required |
| Very High Severity | Review Before Modeling |

Outlier removal is never performed automatically.

---

# Business Examples

## Healthcare

Patient blood glucose

↓

Extreme value detected

↓

Potential medical emergency

↓

Investigate

---

## Finance

Transaction Amount

↓

Unusually high payment

↓

Potential fraud

↓

Flag for review

---

## Retail

Purchase Value

↓

Very large order

↓

VIP customer or data error

↓

Business validation

---

## Manufacturing

Machine Temperature

↓

Extreme sensor reading

↓

Potential equipment failure

↓

Maintenance inspection

---

# Current Implementation

Current Version

CLASSIFIC-AI currently implements:

- IQR Detection
- Z-Score Detection
- Modified Z-Score Detection
- Consensus Detection
- Severity Classification
- AI Recommendation Engine

Future versions will include:

- Isolation Forest

- Local Outlier Factor

- DBSCAN

- One-Class SVM

- Interactive Outlier Dashboard

- Time-Series Outlier Detection

- AI-powered Anomaly Explanation

---

# Human Approval

Outlier recommendations are never executed automatically.

Users may:

- Retain outliers

- Remove observations

- Modify thresholds

- Ignore recommendations

- Apply business-specific rules

Every decision should be documented for governance and auditability.

---

# Best Practices

✔ Investigate before removing outliers

✔ Use multiple detection methods

✔ Validate with business experts

✔ Review feature distributions

✔ Document all decisions

✔ Preserve business-critical anomalies

---

# Common Mistakes

Avoid:

- Automatically removing all outliers

- Using only one detection method

- Ignoring business context

- Applying Z-Score to highly skewed data

- Removing fraud signals

---

# Future Enhancements

Version 2.0

Future improvements include:

- AI-powered anomaly explanation

- Automatic threshold optimization

- Industry-specific anomaly detection

- Time-Series anomaly detection

- Interactive Streamlit dashboard

- Cross-feature anomaly analysis

---

# References

- Tukey (1977)

- Iglewicz & Hoaglin (1993)

- SciPy Documentation

- CRISP-DM Methodology

---

# Interaction with Other Modules

The Outlier module provides foundational information for:

- Distribution Analysis

- Feature Quality

- Profiling Recommendation

- Executive Profiling Report

- Feature Engineering Agent

- Model Recommendation Agent

- Simulation Agent

The outputs generated by this module help improve preprocessing, model robustness, and explainability throughout the CLASSIFIC-AI pipeline.

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
