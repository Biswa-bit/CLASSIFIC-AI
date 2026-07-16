# Profiling Readiness Decision Logic

---

# Overview

This document describes how CLASSIFIC-AI determines whether a dataset is ready to proceed from the Data Profiling Agent to the next stage of the machine learning pipeline.

Rather than relying on a single metric, the Profiling Readiness Engine evaluates multiple profiling dimensions and combines them into an explainable readiness assessment.

The decision logic provides transparent recommendations and supports human approval before model development begins.

---

# Purpose

The objectives are to:

- Evaluate overall profiling health
- Detect critical risks
- Prioritize preprocessing actions
- Reduce model risk
- Improve explainability
- Support governance

---

# Inputs

The decision engine consumes outputs from:

- Dataset Overview
- Column Intelligence
- Statistics Summary
- Feature Quality
- Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Profiling Recommendation Engine

---

# Evaluation Dimensions

CLASSIFIC-AI evaluates:

- Data Quality
- Feature Quality
- Missing Values
- Distribution
- Correlation
- Outliers
- Business Constraints
- Dataset Completeness

---

# Decision Logic

The engine evaluates every profiling result.

Example

IF

Missing Values <5%

AND

No Critical Outliers

AND

Good Feature Quality

↓

Proceed

---

IF

Missing Values >30%

↓

Recommend Missing Value Treatment

---

IF

High Correlation Detected

↓

Recommend Correlation Review

---

IF

Constant Features Detected

↓

Recommend Feature Removal

---

IF

Identifier Columns Detected

↓

Exclude From Modeling

---

IF

Poor Feature Quality

↓

Human Review Required

---

# Readiness Categories

| Score | Recommendation |
|--------|----------------|
| 90–100 | Ready |
| 75–89 | Minor Improvements |
| 60–74 | Requires Preprocessing |
| Below 60 | Not Ready |

---

# Recommendation Priority

Priority 1

Critical

- Invalid Data
- Missing Target
- Corrupted Dataset

Priority 2

High

- High Missing Values
- Severe Outliers
- Duplicate Records

Priority 3

Medium

- Distribution Issues
- High Correlation
- Cardinality

Priority 4

Low

- Cosmetic Improvements
- Formatting

---

# Business Decision Logic

The engine never considers statistics alone.

Business importance is also evaluated.

Example

Customer_ID

↓

Identifier

↓

Remove

Patient_ID

↓

Identifier

↓

Keep for Traceability

↓

Exclude only from ML

---

# Human Approval

Automatic actions are never performed.

Users may:

- Accept recommendation
- Reject recommendation
- Override thresholds
- Apply business rules

---

# Future Enhancements

Version 2.0

Future improvements

- AI Readiness Scoring

- Business Risk Scoring

- Simulation Readiness

- Industry-specific Logic

- LLM-assisted Recommendations

- Continuous Learning Engine

---

# Interaction with Other Modules

Feeds directly into:

- Preprocessing Agent
- Business Rules Agent
- EDA Agent
- Feature Engineering Agent
- Model Recommendation Agent
- RAG Agent
- AI Copilot

---

# Version

Current Version: 1.0

Planned Version: 2.0

---

# Author

Biswadip Choudhury

---

# Project

CLASSIFIC-AI

Open Source Intelligent Machine Learning Framework
