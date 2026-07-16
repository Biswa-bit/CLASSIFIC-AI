# Column Intelligence

---

# Overview

Column Intelligence is one of the core modules within the CLASSIFIC-AI Data Profiling Agent.

Its purpose is to understand every feature (column) in the dataset before any statistical analysis begins.

Instead of treating every column equally, Column Intelligence automatically classifies columns according to their characteristics, business meaning, statistical properties, and machine learning suitability.

This module acts as the "brain" of the profiling process by generating rich metadata that is reused throughout the entire CLASSIFIC-AI pipeline.

---

# Purpose

The objectives of the Column Intelligence module are:

- Identify every column
- Detect column data type
- Determine semantic meaning
- Measure uniqueness
- Identify missing values
- Detect constant features
- Detect identifiers
- Detect high-cardinality columns
- Estimate feature importance
- Recommend downstream profiling modules

---

# Why Column Intelligence is Important

Not every column should receive the same treatment.

Examples:

Employee_ID

should never be scaled.

Country

requires encoding.

Salary

requires statistical analysis.

Review_Text

requires NLP preprocessing.

Without understanding the role of each feature, incorrect preprocessing decisions may occur.

Column Intelligence ensures every feature follows the correct analytical path.

---

# Information Generated

For every column, the module produces:

- Column Name
- Data Type
- Business Type
- Missing Percentage
- Unique Values
- Cardinality
- Constant Feature Status
- Identifier Status
- Numerical/Categorical Classification
- Recommended Analysis
- Risk Level

---

# Column Categories

The module classifies columns into categories such as:

### Numerical

Examples

- Age
- Salary
- Income
- Revenue

---

### Categorical

Examples

- Department
- Country
- Gender
- Product Category

---

### Boolean

Examples

- Purchased
- Active
- Fraud

---

### DateTime

Examples

- Joining Date
- Invoice Date
- Transaction Date

---

### Text

Examples

- Review
- Comments
- Description

---

### Identifier

Examples

- Employee_ID
- Customer_ID
- Invoice_Number

Identifiers are excluded from most machine learning models.

---

# Metadata Produced

Example

| Attribute | Example |
|------------|----------|
| Column | Salary |
| Data Type | Float |
| Missing | 2% |
| Unique Values | 842 |
| Category | Numerical |
| Recommendation | Statistical Analysis |

---

# CLASSIFIC-AI Decision Logic

The Column Intelligence module recommends actions using predefined decision rules.

Examples

| Condition | Recommendation |
|-----------|----------------|
| Numeric | Statistics Summary |
| Categorical | Cardinality Analysis |
| Date | Date Analysis |
| Text | NLP Recommendation |
| Identifier | Exclude from Modeling |
| Constant Feature | Remove Feature |

---

# Business Examples

## Healthcare

Patient_ID

↓

Identifier

↓

Exclude from Modeling

Age

↓

Numerical

↓

Distribution Analysis

Diagnosis

↓

Categorical

↓

Encoding Recommendation

---

## Finance

Transaction_ID

↓

Identifier

↓

Remove from Modeling

Amount

↓

Numerical

↓

Outlier Detection

Risk Category

↓

Categorical

↓

Encoding Recommendation

---

## Retail

Product_ID

↓

Identifier

↓

Exclude

Price

↓

Numerical

↓

Distribution Analysis

Product Description

↓

Text

↓

NLP Analysis

---

# Current Implementation

Current Version

The module identifies:

- Numerical columns
- Categorical columns
- Identifier columns
- Missing values
- High-cardinality columns
- Constant features

Future versions will include:

- Automatic semantic detection
- AI-powered feature understanding
- Industry-specific feature classification
- Metadata quality scoring

---

# Human Approval

Users may:

- Override detected column type
- Reclassify features
- Exclude columns
- Add business labels
- Lock feature definitions

---

# Best Practices

✔ Validate detected data types

✔ Verify identifier columns

✔ Remove constant features

✔ Review high-cardinality variables

✔ Add business descriptions

---

# Common Mistakes

Avoid:

- Treating identifiers as predictive features

- Ignoring text columns

- Incorrectly classifying dates

- Ignoring business meaning

---

# Future Enhancements

Version 2.0

Planned features:

- AI Feature Understanding

- Automatic Business Metadata

- Industry Feature Templates

- Feature Lineage Tracking

- Knowledge Graph Integration

---

# References

- Pandas Documentation

- Python Data Model

- CRISP-DM Methodology

---

# Interaction with Other Modules

Column Intelligence provides metadata used by:

- Dataset Overview
- Statistics Summary
- Feature Quality
- Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Profiling Recommendation
- Executive Profiling Report

Without this module, downstream profiling modules cannot correctly determine which analyses should be performed on each feature.

---

# Related Agents

This module contributes knowledge to:

- Data Profiling Agent
- EDA Agent
- Business Rules Agent
- Feature Engineering Agent
- Feature Selection Agent

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
