# Dataset Validation

## Purpose

Dataset validation ensures that the uploaded dataset is suitable for machine learning before preprocessing begins.

---

## Current Validation

The Dataset Agent validates:

✓ Dataset successfully loaded

✓ Dataset Shape

✓ Dataset Information

✓ Missing Values

✓ Duplicate Rows

---

## Validation Workflow

Dataset Loaded

↓

Display Shape

↓

Display Dataset Information

↓

Check Missing Values

↓

Check Duplicate Rows

↓

Validation Complete

↓

Pass to Preprocessing Agent

---

## Output

The Dataset Agent reports

- Number of Rows
- Number of Columns
- Data Types
- Missing Values
- Duplicate Rows

---

## Best Practices

- Remove unnecessary blank rows.
- Ensure headers exist.
- Avoid duplicate column names.
- Use meaningful column names.

---

## Planned Validation

Version 1.1

- Empty Dataset Detection
- Duplicate Column Detection
- Mixed Data Type Detection

Version 2.0

- Schema Validation
- Data Drift Detection
- Automatic Metadata Extraction

---

Author

Biswadip Choudhury

CLASSIFIC-AI
