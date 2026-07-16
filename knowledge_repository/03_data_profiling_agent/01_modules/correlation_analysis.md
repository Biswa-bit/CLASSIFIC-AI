# Correlation Analysis

---

# Overview

Correlation Analysis is one of the core modules within the CLASSIFIC-AI Data Profiling Agent.

The purpose of this module is to measure the strength and direction of relationships between numerical features in a dataset.

Understanding feature relationships helps identify multicollinearity, redundant variables, hidden dependencies, and opportunities for feature engineering.

The Correlation Analysis module provides explainable insights that support Feature Selection, Business Rules, Feature Engineering, and Model Recommendation.

---

# Purpose

The objectives of the Correlation Analysis module are:

- Measure relationships between features
- Detect multicollinearity
- Identify redundant variables
- Improve feature selection
- Support feature engineering
- Reduce model complexity
- Improve model interpretability
- Generate explainable AI recommendations

---

# Why Correlation Analysis is Important

Highly correlated variables often contain similar information.

Keeping multiple highly correlated features may lead to:

- Multicollinearity
- Unstable model coefficients
- Reduced model interpretability
- Increased computational complexity
- Redundant information

Understanding feature relationships enables better preprocessing and feature selection decisions.

---

# Correlation Methods

Current Version

The module currently computes:

- Pearson Correlation

Future versions will support:

- Spearman Correlation
- Kendall Rank Correlation
- Point-Biserial Correlation
- Phi Coefficient
- Cramér's V (Categorical Features)
- Mutual Information

---

# Correlation Strength Interpretation

The absolute correlation coefficient is interpreted as:

| Absolute Correlation | Strength |
|----------------------|----------|
| 0.90 – 1.00 | Very Strong |
| 0.70 – 0.89 | Strong |
| 0.50 – 0.69 | Moderate |
| 0.30 – 0.49 | Weak |
| 0.00 – 0.29 | Very Weak |

---

# Correlation Direction

Positive Correlation

As one feature increases, the other feature also tends to increase.

Example

Years of Experience

↓

Salary

---

Negative Correlation

As one feature increases, the other feature tends to decrease.

Example

Discount

↓

Profit Margin

---

No Correlation

The variables do not show any meaningful linear relationship.

---

# Example Output

| Feature 1 | Feature 2 | Correlation | Strength | Direction |
|------------|-----------|-------------|-----------|------------|
| Age | Salary | 0.82 | Strong | Positive |
| Discount | Profit | -0.74 | Strong | Negative |
| Customer_ID | Revenue | 0.04 | Very Weak | No Meaningful Relationship |

---

# CLASSIFIC-AI Decision Logic

The Correlation Analysis module applies predefined recommendation rules.

| Condition | Recommendation |
|-----------|----------------|
| Absolute Correlation ≥ 0.90 | Consider removing one feature to reduce multicollinearity |
| Absolute Correlation 0.70–0.89 | Review business importance before modeling |
| Absolute Correlation 0.50–0.69 | Moderate correlation, generally acceptable |
| Absolute Correlation < 0.50 | No action required |

Recommendations are generated automatically but require human review before feature removal.

---

# Business Examples

## Healthcare

Height

↓

Weight

↓

Strong Positive Correlation

↓

Review before modeling

---

## Finance

Income

↓

Loan Amount

↓

Moderate Positive Correlation

↓

Acceptable Relationship

---

## Retail

Discount

↓

Profit

↓

Strong Negative Correlation

↓

Business Insight

---

## Manufacturing

Machine Temperature

↓

Machine Pressure

↓

Strong Positive Correlation

↓

Investigate Equipment Relationship

---

# Current Implementation

Current Version

The module computes:

- Pearson Correlation Matrix
- Pairwise Feature Comparison
- Correlation Strength
- Correlation Direction
- AI Recommendations

Future versions will include:

- Correlation Heatmaps
- Interactive Correlation Explorer
- Partial Correlation
- Categorical Correlation
- Correlation Network Graph
- Automatic Multicollinearity Detection using VIF

---

# Human Approval

Users may:

- Review correlated feature pairs
- Accept AI recommendations
- Retain correlated features for business reasons
- Remove redundant variables
- Override correlation thresholds

Human approval is required before removing any feature solely due to correlation.

---

# Best Practices

✔ Review highly correlated feature pairs

✔ Consider business meaning before removing variables

✔ Validate relationships using domain knowledge

✔ Combine correlation analysis with VIF analysis

✔ Monitor multicollinearity during feature engineering

---

# Common Mistakes

Avoid:

- Removing features based only on correlation

- Assuming correlation implies causation

- Ignoring business importance

- Ignoring nonlinear relationships

- Removing variables without validating model performance

---

# Future Enhancements

Version 2.0

Planned features:

- Spearman Correlation

- Kendall Correlation

- Categorical Correlation

- Mutual Information

- Correlation Heatmaps

- Correlation Network Visualization

- Automatic Multicollinearity Detection

- AI-powered Correlation Interpretation

---

# References

- Pandas Documentation

- NumPy Documentation

- SciPy Statistics Documentation

- CRISP-DM Methodology

- Applied Multivariate Statistical Analysis

---

# Interaction with Other Modules

Correlation Analysis provides relationship insights used by:

- Statistics Summary
- Feature Quality
- Distribution Analysis
- Outlier Detection
- Profiling Recommendation Engine
- Executive Profiling Report

The correlation results are further utilized by downstream agents for feature selection, multicollinearity assessment, feature engineering, and model recommendation.

---

# Related Agents

This module contributes knowledge to:

- Data Profiling Agent
- EDA Agent
- Business Rules Agent
- Feature Engineering Agent
- Feature Selection Agent
- Model Recommendation Agent
- Explainability Agent

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
