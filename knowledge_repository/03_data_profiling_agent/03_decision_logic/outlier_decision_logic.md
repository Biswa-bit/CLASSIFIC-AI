# Outlier Decision Logic

---

# Overview

This document describes how CLASSIFIC-AI evaluates outliers and generates intelligent recommendations before preprocessing and machine learning.

Rather than automatically removing unusual observations, the Outlier Decision Engine combines multiple statistical methods with business context to determine whether an observation should be retained, investigated, or removed.

Every recommendation is transparent, explainable, and requires human approval before implementation.

---

# Purpose

The objectives are to:

- Detect abnormal observations
- Improve data quality
- Reduce model bias
- Preserve business-critical anomalies
- Improve explainability
- Support business investigations
- Improve model robustness
- Enable human governance

---

# Inputs

The Outlier Decision Engine consumes outputs from:

- Dataset Overview
- Statistics Summary
- Distribution Analysis
- Feature Quality Assessment
- Outlier Detection Module
- Business Rules

---

# Evaluation Dimensions

CLASSIFIC-AI evaluates:

- IQR Outliers
- Z-Score Outliers
- Modified Z-Score Outliers
- Consensus Outlier Detection
- Outlier Severity
- Feature Importance
- Business Criticality
- Distribution Characteristics

---

# Decision Logic

The engine evaluates every numerical feature independently.

---

## No Outliers

IF

Consensus Outlier Count = 0

↓

Feature Healthy

↓

No Action Required

---

## Very Low Outlier Percentage

IF

Outlier Percentage <1%

↓

Natural Variation

↓

Retain Data

---

## Low Outlier Percentage

IF

Outlier Percentage between 1% and 5%

↓

Review Feature

↓

No Automatic Removal

---

## Moderate Outlier Percentage

IF

Outlier Percentage between 5% and 10%

↓

Business Investigation Recommended

↓

Review Before Modeling

---

## High Outlier Percentage

IF

Outlier Percentage between 10% and 20%

↓

Human Review Required

↓

Investigate Root Cause

---

## Very High Outlier Percentage

IF

Outlier Percentage >20%

↓

Critical Investigation

↓

Review Data Collection Process

↓

Possible Data Quality Issue

---

## Consensus Detection

IF

Observation detected by:

- IQR

AND

- Z-Score

AND

- Modified Z-Score

↓

High Confidence Outlier

↓

Business Review Required

---

## Single Method Detection

IF

Detected by only one statistical method

↓

Low Confidence

↓

Monitor Only

---

## Business Critical Observation

IF

Observation is Business Critical

↓

Retain Observation

↓

Exclude Automatic Removal

Examples

- Fraudulent Transaction
- Rare Disease
- Equipment Failure
- VIP Customer Purchase

---

## Measurement Error

IF

Business Validation confirms:

- Sensor Failure
- Data Entry Error
- Corrupted Record

↓

Recommend Removal

---

# Outlier Severity Categories

| Outlier Percentage | Severity | Recommendation |
|-------------------|----------|----------------|
| 0% | None | Proceed |
| <1% | Very Low | Retain |
| 1–5% | Low | Review |
| 5–10% | Moderate | Investigate |
| 10–20% | High | Human Review |
| >20% | Critical | Root Cause Analysis |

---

# Recommendation Priority

Priority 1

Critical

- Corrupted Data
- Measurement Errors
- Sensor Failures
- Invalid Observations

---

Priority 2

High

- Consensus Outliers
- High Severity
- Business Risk

---

Priority 3

Medium

- Moderate Outlier Percentage
- Distribution Shift

---

Priority 4

Low

- Natural Extreme Values

---

# Business Decision Logic

Outlier decisions are never based solely on statistics.

Business meaning is always evaluated.

---

Healthcare

Blood Pressure

↓

Extremely High

↓

Potential Medical Emergency

↓

Retain

↓

Investigate

---

Finance

Transaction Amount

↓

Very Large

↓

Potential Fraud

↓

Retain

↓

Flag for Investigation

---

Retail

Purchase Value

↓

Extremely High

↓

VIP Customer

↓

Retain

↓

Business Validation

---

Manufacturing

Machine Temperature

↓

Extreme Reading

↓

Potential Equipment Failure

↓

Maintenance Inspection

↓

Retain

---

# Human Approval

Outlier recommendations are never executed automatically.

Users may:

- Accept recommendations

- Reject recommendations

- Modify thresholds

- Retain business anomalies

- Remove corrupted observations

- Apply organization-specific policies

Human approval is mandatory before removing any observations.

---

# Explainability

Every recommendation includes:

- Detection Method

- Number of Detection Methods

- Outlier Severity

- Statistical Evidence

- Business Interpretation

- Confidence Level

- Recommended Action

- Expected Model Impact

This ensures every decision made by CLASSIFIC-AI is transparent, explainable, and auditable.

---

# Future Enhancements

Version 2.0

Future improvements include:

- Isolation Forest

- Local Outlier Factor (LOF)

- DBSCAN

- One-Class SVM

- AI-powered Root Cause Analysis

- Time-Series Anomaly Detection

- Industry-specific Outlier Rules

- Continuous Anomaly Monitoring

---

# Interaction with Other Modules

This decision engine supports:

- Preprocessing Agent

- Business Rules Agent

- Feature Engineering Agent

- Model Recommendation Agent

- Simulation Agent

- Explainability Agent

- Monitoring Agent

- RAG Agent

- AI Copilot

The recommendations generated here guide preprocessing decisions, business investigations, anomaly handling, and model optimization throughout the CLASSIFIC-AI pipeline.

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
