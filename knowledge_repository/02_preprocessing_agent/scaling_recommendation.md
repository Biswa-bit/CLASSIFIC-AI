# Scaling Recommendation

---

# Overview

Scaling Recommendation is an intelligent preprocessing module within the CLASSIFIC-AI Preprocessing Agent.

Many machine learning algorithms perform better when numerical features are transformed to a similar scale. The Scaling Recommendation module automatically analyzes numerical features, identifies whether scaling is required, and recommends the most appropriate scaling technique.

The module follows the recommendation-first philosophy of CLASSIFIC-AI. Feature scaling is never applied automatically. Instead, the module explains the recommendation and requests human approval before execution.

---

# Purpose

The objectives of the Scaling Recommendation module are:

- Detect numerical features
- Analyze feature distributions
- Recommend appropriate scaling techniques
- Improve model convergence
- Reduce feature dominance
- Enhance model performance

---

# Why Scaling is Important

Machine learning algorithms calculate distances, gradients, or optimization functions using numerical values.

When numerical features have significantly different ranges, larger values may dominate smaller ones, leading to biased model behavior.

Example

| Feature | Range |
|----------|-------|
| Age | 18–65 |
| Salary | 20,000–2,000,000 |

Without scaling, Salary may disproportionately influence the model.

Scaling improves learning efficiency and model stability.

---

# Algorithms That Require Scaling

Scaling is recommended for:

- Logistic Regression
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Neural Networks
- K-Means Clustering
- Principal Component Analysis (PCA)

---

# Algorithms That Usually Do Not Require Scaling

Tree-based algorithms are generally insensitive to feature scaling.

Examples

- Decision Tree
- Random Forest
- Extra Trees
- XGBoost
- LightGBM
- CatBoost

Although scaling is not required, it may still be applied for consistency within a pipeline.

---

# Supported Scaling Techniques

## StandardScaler

Formula

```
Z = (X − μ) / σ
```

Characteristics

- Mean becomes 0
- Standard deviation becomes 1

Recommended when

- Data follows approximately normal distribution
- No significant outliers

---

## MinMaxScaler

Formula

```
(X − Min)

/

(Max − Min)
```

Output Range

0 to 1

Recommended when

- Neural Networks
- Distance-based algorithms
- Features need bounded values

---

## RobustScaler

Uses

- Median
- Interquartile Range (IQR)

Recommended when

- Dataset contains significant outliers
- Distribution is skewed

RobustScaler is less influenced by extreme values.

---

## MaxAbsScaler

Scales values using the maximum absolute value.

Recommended when

- Sparse datasets
- Features centered around zero

---

## Normalizer

Normalizes each sample to unit norm.

Recommended for

- Text mining
- Cosine similarity
- Document classification

---

# CLASSIFIC-AI Recommendation Logic

The module evaluates:

- Numerical data type
- Presence of outliers
- Distribution shape
- Skewness
- Selected machine learning algorithm

Based on these characteristics, the module recommends the most suitable scaling method.

---

# Recommendation Rules

| Dataset Characteristic | Recommended Scaler |
|-------------------------|-------------------|
| Normal Distribution | StandardScaler |
| Features with Fixed Range | MinMaxScaler |
| Significant Outliers | RobustScaler |
| Sparse Data | MaxAbsScaler |
| Text Vectors | Normalizer |

---

# Current Implementation

Current Version

The module recommends:

- StandardScaler
- MinMaxScaler
- RobustScaler

Future versions will include:

- MaxAbsScaler
- Normalizer
- QuantileTransformer
- PowerTransformer

---

# Human Approval

Scaling is never performed automatically.

The user decides whether to:

- Accept the recommendation
- Choose a different scaler
- Skip scaling
- Apply business-specific preprocessing

---

# Best Practices

✔ Scale only numerical features

✔ Fit the scaler using training data only

✔ Apply the same scaler to validation and test datasets

✔ Review feature distributions before selecting a scaler

✔ Preserve the fitted scaler for production deployment

---

# Common Mistakes

Avoid:

- Scaling the target variable unnecessarily

- Fitting the scaler on the entire dataset before splitting

- Using StandardScaler when extreme outliers exist

- Scaling categorical variables

---

# Future Enhancements

Version 2.0

Planned features:

- Automatic distribution detection

- QuantileTransformer

- PowerTransformer

- Adaptive scaling recommendation

- AI-based scaler selection

- Scaling performance comparison

---

# Interaction with Other Modules

Scaling Recommendation works closely with:

- Outlier Detection

- Data Profiling Agent

- Feature Engineering Agent

- Model Recommendation Agent

- Recommendation Engine

Scaling recommendations should be finalized before model training.

---

# Related Documentation

- outlier_detection.md

- datatype_detection.md

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
