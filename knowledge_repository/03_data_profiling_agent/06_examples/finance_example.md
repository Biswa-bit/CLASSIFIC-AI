# Finance Data Profiling Example

---

# Overview

This example demonstrates how the CLASSIFIC-AI Data Profiling Agent analyzes a financial dataset before machine learning model development.

The objective is to identify data quality issues, evaluate statistical characteristics, generate explainable recommendations, and determine whether the dataset is ready for credit risk prediction, fraud detection, or financial forecasting.

---

# Business Scenario

A financial institution wants to develop a machine learning model to predict customer loan default.

Before feature engineering and model development, the dataset must undergo comprehensive data profiling.

---

# Dataset

Example Dataset

Loan Default Prediction

Features

- Customer ID
- Age
- Annual Income
- Employment Status
- Loan Amount
- Credit Score
- Existing Debt
- Loan Term
- Number of Previous Loans
- Default Status

Records

75,000

---

# Profiling Results

## Dataset Overview

Rows

75,000

Columns

10

Missing Values

6.8%

Duplicate Records

35

Memory Usage

5.4 MB

---

## Statistics Summary

Annual Income

Mean = 62,450

Median = 54,800

Standard Deviation = 28,900

Loan Amount

Mean = 285,000

Median = 210,000

Standard Deviation = 165,000

---

## Feature Quality

Overall Feature Quality Score

91%

Low Quality Features

- Employment Status

Reason

Missing Values

---

## Distribution Analysis

Annual Income

Highly Right Skewed

Recommendation

Log Transformation

---

Loan Amount

Heavy-Tailed Distribution

Recommendation

RobustScaler

---

Credit Score

Approximately Normal

Recommendation

No Transformation Required

---

## Correlation Analysis

Loan Amount

Existing Debt

Correlation

0.88

Recommendation

Business Review

---

Annual Income

Credit Score

Correlation

0.42

Recommendation

Retain Both Features

---

## Outlier Detection

Loan Amount

Outliers Detected

3.6%

Recommendation

Business Investigation

Large commercial loans should be retained.

---

Annual Income

Outliers

1.8%

Recommendation

Manual Validation

---

## Missing Values

Employment Status

Missing

7%

Recommendation

Mode Imputation

---

Annual Income

Missing

2%

Recommendation

Median Imputation

---

# Data Quality Assessment

Dataset Quality Score

90%

Status

Excellent

---

# Dataset Readiness

Readiness Score

92%

Status

Production Ready

Recommendation

Proceed to Exploratory Data Analysis (EDA)

---

# Business Recommendations

✓ Apply Log Transformation to Annual Income

✓ Apply RobustScaler to Loan Amount

✓ Retain high-value commercial loan records after validation

✓ Review correlation between Loan Amount and Existing Debt

✓ Impute missing Employment Status values

✓ Proceed to Feature Engineering after EDA

---

# Risk Assessment

Overall Risk Level

Low

Identified Risks

- Moderate Missing Values

- High Loan Amount Outliers

- Strong Correlation between Loan Amount and Existing Debt

Overall Recommendation

Proceed after minor preprocessing.

---

# Human Approval

Required Actions

✓ Approve Missing Value Treatment

✓ Approve Scaling Recommendations

✓ Review Business-Critical Loan Records

✓ Approve Dataset Readiness

---

# Lessons Learned

Financial datasets often contain:

- Right-skewed income distributions

- Large but legitimate commercial loans

- Strong relationships between financial variables

Business context is essential before removing observations or modifying variables.

---

# Related Modules

- Dataset Overview

- Statistics Summary

- Distribution Analysis

- Correlation Analysis

- Outlier Detection

- Feature Quality

- Dataset Readiness

- Risk Assessment

- Deployment Readiness

- EDA Agent

---

# Version

Current Version: **1.0**

---

# Author

**Biswadip Choudhury**

---

# Project

**CLASSIFIC-AI**

**Open Source Intelligent Machine Learning Framework**