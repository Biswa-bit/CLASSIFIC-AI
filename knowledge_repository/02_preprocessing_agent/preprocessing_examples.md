# Preprocessing Examples

---

# Overview

The Preprocessing Examples document demonstrates how the CLASSIFIC-AI Preprocessing Agent analyzes real-world datasets and generates intelligent preprocessing recommendations.

Unlike the technical documentation for individual modules, this document illustrates complete preprocessing workflows using practical examples from multiple domains.

These examples help users understand how preprocessing recommendations are generated and why different datasets require different preprocessing strategies.

---

# Purpose

The objectives of this document are:

- Demonstrate preprocessing using real datasets
- Explain recommendation logic
- Show business reasoning
- Improve user understanding
- Support learning and onboarding

---

# Example 1 — Glassdoor Dataset

## Dataset

Job Review Dataset

Rows

505

Columns

18

---

## Observations

| Issue | Status |
|---------|---------|
| Duplicate Rows | No |
| Missing Values | Salary Column |
| Text Columns | Job Description |
| Numerical Columns | Company Rating |
| Categorical Columns | Industry, Location |
| Date Columns | None |
| Identifier Columns | None |

---

## CLASSIFIC-AI Recommendations

| Module | Recommendation |
|---------|----------------|
| Missing Values | Median Imputation |
| Text Detection | Sentence Embeddings |
| Encoding | One-Hot Encoding |
| Scaling | StandardScaler |
| Dataset Health | Good |

---

## Reasoning

The dataset contains long text descriptions that are suitable for embedding-based NLP techniques. Company ratings are numerical and approximately normally distributed, making StandardScaler an appropriate recommendation.

---

# Example 2 — Titanic Dataset

## Dataset

Passenger Survival Prediction

---

## Observations

- Missing Age values
- Missing Cabin values
- Categorical variables
- Identifier column (PassengerId)

---

## Recommendations

| Module | Recommendation |
|---------|----------------|
| Missing Values | Median / Mode |
| Cabin | Business Review |
| Encoding | One-Hot Encoding |
| PassengerId | Exclude from Model |
| Scaling | StandardScaler |

---

## Reasoning

PassengerId uniquely identifies passengers and should not be used for prediction. Cabin contains substantial missing data and requires business review before removal or imputation.

---

# Example 3 — HR Employee Attrition

## Dataset

Employee Attrition Prediction

---

## Observations

- Department
- Job Role
- Monthly Income
- Overtime
- Employee Number

---

## Recommendations

| Module | Recommendation |
|---------|----------------|
| Employee Number | Exclude |
| Overtime | Boolean Conversion |
| Department | One-Hot Encoding |
| Monthly Income | RobustScaler (if outliers exist) |

---

## Reasoning

Employee Number functions as an identifier, while Overtime is a binary feature that should be standardized. Income scaling depends on the presence of outliers.

---

# Example 4 — Customer Churn

## Dataset

Telecom Customer Churn

---

## Observations

- CustomerID
- Contract Type
- Monthly Charges
- Total Charges
- Churn

---

## Recommendations

| Module | Recommendation |
|---------|----------------|
| CustomerID | Exclude |
| Contract Type | One-Hot Encoding |
| Monthly Charges | StandardScaler |
| Churn | Target Variable |

---

## Example 5 — Retail Sales

## Dataset

Retail Transaction Data

---

## Observations

- Product_ID
- Store_ID
- Sales
- Profit
- Order Date

---

## Recommendations

| Module | Recommendation |
|---------|----------------|
| Product_ID | Review Identifier |
| Store_ID | Review Identifier |
| Sales | StandardScaler |
| Order Date | Date Feature Extraction |

---

# Example 6 — Healthcare Dataset

## Dataset

Hospital Patient Records

---

## Observations

- Patient_ID
- Age
- Diagnosis
- Admission Date
- Clinical Notes

---

## Recommendations

| Module | Recommendation |
|---------|----------------|
| Patient_ID | Exclude from Model |
| Clinical Notes | Sentence Embeddings |
| Admission Date | Date Feature Extraction |
| Diagnosis | One-Hot or Target Encoding |

---

# Summary

These examples demonstrate that preprocessing recommendations depend on:

- Data type
- Business context
- Statistical characteristics
- Machine learning objectives

The Recommendation Engine evaluates these factors together before suggesting preprocessing actions.

---

# Best Practices

✔ Validate recommendations before execution

✔ Consider business objectives

✔ Preserve original data

✔ Keep preprocessing reproducible

✔ Review identifier columns carefully

---

# Future Enhancements

Version 2.0

Planned improvements:

- Interactive examples

- Domain-specific workflows

- End-to-end preprocessing case studies

- Visual preprocessing reports

- Streamlit demonstrations

---

# Related Knowledge Assets

- preprocessing_workflow.md
- preprocessing_decision_tree.md
- preprocessing_best_practices.md
- recommendation_engine.md

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
