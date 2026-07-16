# Outlier Detection

---

# Overview

Outlier Detection is one of the core modules within the CLASSIFIC-AI Data Profiling Agent.

The purpose of this module is to identify observations that significantly differ from the majority of the data.

Outliers may represent:

- Data entry errors
- Measurement errors
- Fraudulent transactions
- Rare but valid events
- Business anomalies
- Operational risks

The module applies multiple statistical techniques to provide a robust and explainable assessment of potential outliers.

Rather than relying on a single method, CLASSIFIC-AI combines multiple detection techniques to improve reliability and reduce false positives.

---

# Purpose

The objectives of the Outlier Detection module are:

- Detect abnormal observations
- Compare multiple outlier detection methods
- Improve dataset quality
- Support preprocessing decisions
- Reduce model bias
- Improve explainability
- Assist business investigations
- Generate AI recommendations

---

# Why Outlier Detection is Important

Outliers can significantly influence machine learning models.

Potential impacts include:

- Reduced model accuracy
- Distorted statistical summaries
- Poor regression performance
- Increased prediction errors
- Misleading business insights

However, not all outliers should be removed.

Some outliers represent valuable business events such as:

- Fraud detection
- Equipment failures
- Disease outbreaks
- Market shocks

CLASSIFIC-AI therefore recommends investigation before removal.

---

# Detection Methods

Current Version

The module currently supports:

- Interquartile Range (IQR)
- Z-Score
- Modified Z-Score
- Consensus Outlier Detection

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

Observations outside these bounds are considered potential outliers.

---

# Z-Score

The Z-Score measures how many standard deviations an observation lies from the mean.

Formula

Z = (X − Mean) / Standard Deviation

Typical threshold

|Z| > 3

Suitable for approximately normal distributions.

---

# Modified Z-Score

The Modified Z-Score is a robust alternative that uses the Median Absolute Deviation (MAD).

Formula

Modified Z = 0.6745 × (X − Median) / MAD

Typical threshold

|Modified Z| > 3.5

More reliable for skewed datasets and robust to extreme values.

---

# Consensus Outlier Detection

CLASSIFIC-AI combines multiple detection methods.

For each feature the module reports:

- IQR Outliers
- Z-Score Outliers
- Modified Z-Score Outliers
- Consensus Result

Consensus increases confidence in detected anomalies by requiring agreement across methods.

---

# Severity Levels

| Outlier Percentage | Severity |
|-------------------|----------|
| < 1% | Very Low |
| 1% – 5% | Low |
| 5% – 10% | Moderate |
| 10% – 20% | High |
| > 20% | Very High |

---

# Example Output

| Feature | IQR | Z-Score | Modified Z | Severity |
|----------|-----|----------|------------|----------|
| Salary | 12 | 8 | 10 | Moderate |
| Revenue | 35 | 28 | 31 | High |
| Age | 2 | 1 | 2 | Very Low |

---

# CLASSIFIC-AI Decision Logic

The Outlier Detection module applies predefined decision rules.

| Condition | Recommendation |
|-----------|----------------|
| Very Low Severity | No Action Required |
| Low Severity | Review Feature |
| Moderate Severity | Investigate Business Context |
| High Severity | Human Review Required |
| Very High Severity | Review Before Modeling |

Outlier removal is never performed automatically.

Recommendations require human approval.

---

# Business Examples

## Healthcare

Abnormally High Blood Pressure

↓

Potential Medical Emergency

↓

Investigate

---

## Finance

Unusually Large Transaction

↓

Potential Fraud

↓

Flag for Review

---

## Retail

Extremely High Purchase Amount

↓

VIP Customer or Data Error

↓

Business Investigation

---

## Manufacturing

Extreme Machine Temperature

↓

Potential Equipment Failure

↓

Maintenance Inspection

---

# Current Implementation

Current Version

The module currently implements:

- IQR Outlier Detection
- Z-Score Outlier Detection
- Modified Z-Score Detection
- Consensus Analysis
- Severity Classification
- AI Recommendations

Future versions will include:

- Isolation Forest
- Local Outlier Factor
- DBSCAN
- Interactive Outlier Visualizations
- Time-Series Outlier Detection
- AI-generated Anomaly Explanation

---

# Human Approval

Users may:

- Accept recommendations

- Ignore valid business outliers

- Modify thresholds

- Remove observations

- Retain anomalies

Human approval is mandatory before removing outliers.

---

# Best Practices

✔ Investigate before removing outliers

✔ Use multiple detection methods

✔ Validate with business experts

✔ Review feature distributions

✔ Document all outlier decisions

---

# Common Mistakes

Avoid:

- Automatically removing all outliers

- Using only one detection method

- Ignoring business significance

- Applying Z-Score to highly skewed data

- Removing fraud or anomaly signals

---

# References

- Tukey (1977)

- Iglewicz & Hoaglin (1993)

- SciPy Documentation

- CRISP-DM Methodology

---

# Interaction with Other Modules

Outlier Detection works closely with:

- Statistics Summary
- Distribution Analysis
- Feature Quality
- Correlation Analysis
- Profiling Recommendation
- Executive Profiling Report

The detected outliers influence preprocessing decisions, scaling recommendations, feature engineering, and business rule evaluation.

---

# Related Agents

This module contributes knowledge to:

- Data Profiling Agent
- EDA Agent
- Business Rules Agent
- Feature Engineering Agent
- Model Recommendation Agent
- Simulation Agent

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
