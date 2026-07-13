# ID Detection

---

# Overview

ID Detection is an intelligent preprocessing module within the CLASSIFIC-AI Preprocessing Agent.

Many datasets contain identifier columns such as Customer ID, Employee ID, Transaction ID, Order Number, Invoice Number, Product ID, or Record ID. Although these columns uniquely identify records, they usually do not provide meaningful predictive information for machine learning models.

The ID Detection module automatically identifies identifier features, evaluates their characteristics, and recommends whether they should be excluded from model training.

The module follows the recommendation-first philosophy of CLASSIFIC-AI. Identifier columns are never removed automatically.

---

# Purpose

The objectives of the ID Detection module are:

- Detect identifier columns
- Prevent misleading model training
- Improve feature selection
- Reduce unnecessary computation
- Support downstream feature engineering
- Improve model interpretability

---

# Why ID Detection is Important

Identifier columns are designed to uniquely distinguish records rather than describe them.

Examples include:

- Customer_ID
- Employee_ID
- Order_ID
- Invoice_Number
- Transaction_ID
- Product_Code

These columns generally contain little or no predictive value.

Including them during model training may:

- Increase model complexity
- Introduce unnecessary noise
- Cause overfitting
- Reduce model generalization

Therefore, identifier columns should be reviewed before model training.

---

# Common Identifier Features

Examples

```
Customer_ID

Employee_ID

Order_ID

Invoice_Number

Passport_Number

Social_Security_Number

Vehicle_Number

Account_Number
```

---

# Detection Logic

The module evaluates:

- Number of unique values
- Cardinality percentage
- Column name patterns
- Data type
- Sequential numbering
- Business keywords

Typical identifier keywords include:

- id
- code
- number
- key
- uuid
- reference

---

# Mathematical Concept

Identifier Ratio

```
Identifier Ratio

=

Unique Values

/

Total Rows
```

Example

```
Rows

1000

Unique Values

1000

Identifier Ratio

100%
```

A ratio close to 100% may indicate an identifier column.

---

# CLASSIFIC-AI Recommendation Logic

The module analyzes:

- Unique value percentage
- Naming convention
- Sequential patterns
- Business metadata
- Duplicate frequency

Based on these characteristics, CLASSIFIC-AI recommends whether the feature should be excluded from model training.

---

# Recommendation Rules

| Condition | Recommendation |
|-----------|----------------|
| Unique Values ≈ Total Rows | Review as Identifier |
| Sequential Numbers | Likely Identifier |
| Column Name contains "ID" | Review |
| Business Identifier | Exclude from Training |
| Identifier with Business Meaning | Human Review |

---

# Current Implementation

Current Version

The module detects:

- Identifier columns
- High uniqueness
- Common ID naming conventions

The module recommends:

- Exclude from machine learning
- Retain for reporting and record tracking

Future versions will include:

- Automatic UUID detection
- Composite key detection
- Foreign key recognition
- Database schema integration
- AI-based identifier recognition

---

# Human Approval

Identifier columns are never removed automatically.

The user decides whether to:

- Exclude from model training
- Keep for reporting
- Retain as business reference
- Apply business-specific rules

---

# Best Practices

✔ Keep identifiers for traceability

✔ Exclude identifiers from model features

✔ Preserve primary keys

✔ Verify business importance

✔ Document exclusion decisions

---

# Common Mistakes

Avoid:

- Training models using identifiers

- Treating identifiers as categorical variables

- Applying One-Hot Encoding to identifiers

- Removing identifiers before data auditing

---

# Future Enhancements

Version 2.0

Planned features:

- Composite key detection

- UUID recognition

- Foreign key analysis

- AI-generated identifier confidence score

- Automatic metadata integration

---

# Interaction with Other Modules

ID Detection works closely with:

- Data Type Detection

- High Cardinality Detection

- Feature Selection Agent

- Business Rules Agent

- Recommendation Engine

---

# Related Documentation

- datatype_detection.md

- high_cardinality_detection.md

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
