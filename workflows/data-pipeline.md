---
name: Data Pipeline
description: "Data ingestion, cleaning, analysis, and visualization workflow."
trigger: "/data"
---

# Data Pipeline Workflow

## Step 1: Ingest & Assess
- Load data from CSV/JSON/API/DB. Show shape, schema, and first 5 rows preview.
- Apply `@data-analysis` skill: assess quality, find missing values/outliers/duplicates.

## Step 2: Clean & Analyze
- Handle missing values, outliers, formats (dates/categories), and duplicates.
- Run descriptive stats, correlation, group-by categorical analysis, and time-series decomposition.

## Step 3: Visualize & Predict
- Generate distribution plots, time-series trends, correlation heatmaps, and ranking dashboards.
- Summarize top findings, identify trends, recommend predictive models, and list next steps.

## Tools
- **SQLite / Postgres MCP**: SQL queries on large datasets.
- **Math MCP**: Advanced statistical/mathematical formulas.
- **Python / Jupyter**: Local pandas/numpy/sklearn execution scripts.
- **Sequential Thinking**: Complex multi-step reasoning.
- **Memory MCP / Context7**: Store findings and lookup docs.
