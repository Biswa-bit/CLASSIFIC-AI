# High Cardinality Detection

---

# Overview

High Cardinality Detection is an intelligent preprocessing module within the CLASSIFIC-AI Preprocessing Agent.

Cardinality refers to the number of unique values present in a categorical feature. Features with a large number of unique categories are known as high-cardinality features.

Although these features often contain valuable business information, they can create challenges for preprocessing, feature engineering, model training, and model interpretability.

The High Cardinality Detection module automatically identifies high-cardinality features and recommends the most appropriate preprocessing techniques.

The module follows the recommendation-first philosophy of CLASSIFIC-AI and never performs transformations automatically.

---

# Purpose

The objectives of the High Cardinality Detection module are:

- Detect high-cardinality categorical variables
- Reduce dimensionality
- Improve model efficiency
- Recommend suitable encoding techniques
- Improve feature engineering
- Prevent overfitting

---

# Why High Cardinality Matters

High-cardinality features may generate hundreds or thousands of categories.

Examples include:

- Customer ID
- Product ID
- ZIP Code
- City
- Email Address
- Website URL

If One-Hot Encoding is applied directly, the number of generated features can become extremely large.

Example

```
Country

100 unique values

↓

One-Hot Encoding

↓

100 new columns
```

This increases:

- Memory usage
- Training time
- Model complexity
- Risk of overfitting

---

# Mathematical Concept

Cardinality

```
Cardinality

=

Number of Unique Values
```

Example

```
Total Rows

1000

Unique Cities

420

Cardinality

420
```

---

# Cardinality Levels

| Unique Percentage | Category |
|-------------------|----------|
| Less than 5% | Low Cardinality |
| 5%–50% | Medium Cardinality |
| Greater than 50% | High Cardinality |

These thresholds are configurable.

---

# CLASSIFIC-AI Recommendation Logic

The module evaluates:

- Number of unique values
- Percentage of unique values
- Data type
- Business meaning
- Dataset size

Based on these characteristics, the module recommends an appropriate encoding strategy.

---

# Recommendation Rules

| Cardinality | Recommendation |
|--------------|----------------|
| Low | One-Hot Encoding |
| Medium | Frequency Encoding |
| High | Target Encoding or Embeddings |
| Extremely High | Business Review |

---

# Current Implementation

Current Version

The module detects:

- Unique values
- Cardinality percentage

The module recommends:

- One-Hot Encoding
- Frequency Encoding
- Embeddings

Future versions will include:

- Target Encoding
- Hash Encoding
- Binary Encoding
- Automatic encoding comparison

---

# Human Approval

Encoding decisions are never applied automatically.

The user decides whether to:

- Accept recommendation
- Choose another encoding method
- Remove the feature
- Apply business rules

---

# Best Practices

✔ Understand business meaning before encoding

✔ Review cardinality percentage

✔ Use One-Hot Encoding only for low-cardinality features

✔ Consider embeddings for extremely high-cardinality variables

✔ Monitor model complexity after encoding

---

# Common Mistakes

Avoid:

- Applying One-Hot Encoding to thousands of categories

- Ignoring computational cost

- Removing valuable business information

- Treating identifier columns as categorical features

---

# Future Enhancements

Version 2.0

Planned features:

- Automatic Target Encoding

- Binary Encoding

- Hash Encoding

- Entity Embeddings

- AI-based encoding recommendations

- Feature grouping suggestions

---

# Interaction with Other Modules

High Cardinality Detection works closely with:

- Data Type Detection

- Encoding Recommendation

- ID Detection

- Feature Engineering Agent

- Recommendation Engine

---

# Related Documentation

- encoding_recommendation.md

- datatype_detection.md

- id_detection.md

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
