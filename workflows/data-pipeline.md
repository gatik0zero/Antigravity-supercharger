---
name: Data Pipeline
description: "Data ingestion, cleaning, analysis, and visualization workflow."
trigger: "/data"
---

# Data Pipeline Workflow

## Step 1: Data Ingestion
- Load data from source (CSV, JSON, API, database)
- Display data shape, columns, and types
- Show first 5 rows as preview

## Step 2: Data Quality Assessment
Apply the `@data-analysis` skill:
- Identify missing values and strategy for handling
- Detect outliers
- Check for duplicates
- Validate data types and formats
- Report data quality score

## Step 3: Data Cleaning
Based on quality assessment:
- Handle missing values (impute, interpolate, or drop)
- Remove or cap outliers
- Standardize formats (dates, categories, units)
- Remove duplicates
- Document all transformations

## Step 4: Analysis
- Descriptive statistics for all relevant columns
- Correlation analysis
- Group-by analysis for categorical variables
- Time-series decomposition (if temporal data)
- Anomaly detection

## Step 5: Visualization
Generate appropriate charts:
- Overview dashboard with key metrics
- Distribution plots for numerical features
- Trend lines for time-series data
- Correlation heatmap
- Top N / Bottom N rankings

## Step 6: Insights & Predictions
- Summarize top findings
- Identify patterns and trends
- Suggest predictive models if applicable
- Recommend next steps for deeper analysis

## Tools
- **SQLite MCP / Postgres MCP**: For SQL-based analysis on large datasets
- **Math MCP**: Use for complex statistical/mathematical formulas
- **Jupyter/Python**: Write and execute local python scripts for advanced pandas operations
- **Sequential Thinking**: For complex multi-step analysis
- **Memory MCP**: Store findings for future reference
- **Context7**: Look up pandas/numpy/sklearn documentation
