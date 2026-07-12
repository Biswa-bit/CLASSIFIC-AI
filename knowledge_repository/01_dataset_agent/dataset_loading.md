# Dataset Loading

## Purpose

The Dataset Loading module imports datasets into CLASSIFIC-AI.

The module converts the selected dataset into a Pandas DataFrame for downstream processing.

---

## Current Supported Formats

- CSV (.csv)
- Excel (.xlsx)
- Excel (.xls)

---

## Loading Workflow

User Selects Dataset

↓

Detect File Extension

↓

Load Dataset

↓

Convert to Pandas DataFrame

↓

Pass to Dataset Agent

---

## Current Loader

CSV

```python
pd.read_csv()
```

Excel

```python
pd.read_excel()
```

---

## Output

Returns

- Pandas DataFrame
- Dataset Shape
- Column Names
- Data Types

---

## Best Practices

- Keep datasets inside the datasets folder.
- Use descriptive column names.
- Save Excel files as .xlsx whenever possible.
- Ensure the first row contains headers.

---

## Future Enhancements

Version 1.1

- JSON Loader
- Parquet Loader
- Feather Loader

Version 2.0

- Database Loader
- Cloud Storage Loader
- API Loader

---

Author

Biswadip Choudhury

CLASSIFIC-AI

