# Dataset Agent Knowledge Repository

## Overview

The Dataset Agent is the first agent executed in the CLASSIFIC-AI pipeline.

Its responsibility is to safely load the dataset, validate its structure, perform basic quality checks, and pass a clean Pandas DataFrame to the Preprocessing Agent.

---

## Current Version

Version : v1.0

---

## Responsibilities

The Dataset Agent performs the following tasks:

1. Load dataset
2. Validate dataset
3. Display dataset information
4. Display dataset shape
5. Check missing values
6. Check duplicate rows
7. Return Pandas DataFrame

---

## Documentation

- Dataset Loading
- Supported Formats
- Dataset Validation
- Error Handling

---

## Current Workflow

Dataset

↓

Load Dataset

↓

Validate Dataset

↓

Dataset Information

↓

Missing Value Summary

↓

Duplicate Row Summary

↓

Pass DataFrame to Preprocessing Agent

---

## Current Supported Formats

- CSV (.csv)
- Excel (.xlsx)
- Excel (.xls)

---

## Planned Features

Version 1.1

- JSON Support
- Parquet Support
- Feather Support

Version 2.0

- SQL Databases
- Snowflake
- BigQuery
- AWS S3
- Azure Blob Storage

---

Author

Biswadip Choudhury

CLASSIFIC-AI
