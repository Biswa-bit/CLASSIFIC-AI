# Supply Chain Data Profiling Example

---

# Overview

This example demonstrates how the CLASSIFIC-AI Data Profiling Agent analyzes a supply chain dataset before machine learning model development.

The objective is to evaluate data quality, identify statistical issues, generate explainable recommendations, and determine whether the dataset is suitable for supply chain risk prediction, demand forecasting, inventory optimization, logistics planning, or disruption analysis.

---

# Business Scenario

A global manufacturing company wants to build a machine learning model to predict shipment delays and supply chain disruptions.

Before feature engineering and model development, the supply chain dataset must undergo comprehensive data profiling.

---

# Dataset

Example Dataset

Global Supply Chain Risk Analysis

Features

- Shipment ID
- Supplier ID
- Country
- Product Category
- Transportation Mode
- Lead Time
- Inventory Level
- Demand Forecast
- Crude Oil Price
- Exchange Rate
- Geopolitical Risk Index
- Shipment Delay

Records

150,000

---

# Profiling Results

## Dataset Overview

Rows

150,000

Columns

12

Missing Values

2.6%

Duplicate Records

42

Memory Usage

12.4 MB

---

## Statistics Summary

Lead Time

Mean = 18.7 Days

Median = 17.2 Days

Standard Deviation = 6.4 Days

---

Inventory Level

Mean = 1,245 Units

Median = 1,180 Units

Standard Deviation = 540 Units

---

Crude Oil Price

Mean = $82.30

Median = $80.75

Standard Deviation = $11.20

---

## Feature Quality

Overall Feature Quality Score

95%

Low Quality Features

None

---

## Distribution Analysis

Lead Time

Moderately Right Skewed

Recommendation

Business Review

---

Inventory Level

Approximately Normal

Recommendation

No Transformation Required

---

Crude Oil Price

Highly Right Skewed

Recommendation

Log Transformation

---

Geopolitical Risk Index

Heavy-Tailed Distribution

Recommendation

RobustScaler

---

## Correlation Analysis

Crude Oil Price

Transportation Cost

Correlation

0.84

Recommendation

Retain Both Features

Business Review Recommended

---

Lead Time

Shipment Delay

Correlation

0.88

Recommendation

Strong Business Relationship

Retain Both Variables

---

Inventory Level

Demand Forecast

Correlation

0.72

Recommendation

Review Feature Importance

---

## Outlier Detection

Lead Time

Outliers Detected

2.9%

Recommendation

Investigate Supply Chain Disruptions

Retain legitimate delay events.

---

Inventory Level

Outliers

1.6%

Recommendation

Validate Seasonal Demand Peaks

---

Geopolitical Risk Index

Outliers

2.4%

Recommendation

Review Global Events

Do not remove automatically.

---

## Missing Values

Demand Forecast

Missing

2%

Recommendation

Median Imputation

---

Transportation Mode

Missing

1%

Recommendation

Mode Imputation

---

# Data Quality Assessment

Dataset Quality Score

94%

Status

Excellent

---

# Dataset Readiness

Readiness Score

96%

Status

Production Ready

Recommendation

Proceed to Exploratory Data Analysis (EDA)

---

# Business Recommendations

✓ Review shipment delay records before removal

✓ Apply Log Transformation to Crude Oil Price

✓ Apply RobustScaler to Geopolitical Risk Index

✓ Validate seasonal inventory spikes

✓ Review strong relationships between lead time and shipment delay

✓ Continue to Feature Engineering after EDA

---

# Risk Assessment

Overall Risk Level

Low

Identified Risks

- Moderate shipment delay outliers

- Strong feature correlations

- Minor missing values

Overall Recommendation

Dataset suitable for supply chain analytics after minor preprocessing.

---

# Human Approval

Required Actions

✓ Approve Missing Value Treatment

✓ Validate Supply Chain Disruptions

✓ Review Geopolitical Risk Events

✓ Approve Dataset Readiness

---

# Lessons Learned

Supply chain datasets frequently contain:

- Transportation delays

- Seasonal inventory fluctuations

- Demand spikes

- Commodity price volatility

- Exchange rate movements

- Geopolitical disruptions

These observations often represent genuine business events rather than poor data quality and should be investigated before modification or removal.

---

# Future Integration

This dataset can later be enhanced using:

- Business Rules Agent

- Simulation Agent

- Monte Carlo Simulation

- External Economic Indicators

- Weather APIs

- Port Congestion Data

- Commodity Price APIs

- Geopolitical Event Feeds

These enhancements will enable CLASSIFIC-AI to support advanced supply chain risk analysis and scenario simulation.

---

# Related Modules

- Dataset Overview

- Statistics Summary

- Feature Quality

- Distribution Analysis

- Correlation Analysis

- Outlier Detection

- Missing Value Analysis

- Data Quality Assessment

- Deployment Readiness

- Business Rules Agent

- Simulation Agent

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
