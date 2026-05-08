---
name: Data Analysis
description: "Analyze datasets (CSV, JSON, Excel) with statistical methods, visualization recommendations, and ML insights."
---

# Data Analysis Skill

## Trigger
Use this skill when working with data files, asked to analyze data, generate insights, or build visualizations.

## Process

### 1. Data Ingestion
- Load the dataset and display: shape, columns, dtypes
- Show first 5 rows as a preview
- Report: null counts, unique values per column, basic stats

### 2. Exploratory Data Analysis (EDA)
- **Numerical columns**: mean, median, std, min, max, quartiles, distribution shape
- **Categorical columns**: value counts, cardinality, mode
- **Correlations**: Pearson/Spearman correlation matrix for numerical features
- **Outliers**: IQR method or Z-score detection
- **Time-based**: trends, seasonality, stationarity tests (if datetime column exists)

### 3. Data Quality Report
```
| Column | Type | Nulls | Unique | Issues |
|--------|------|-------|--------|--------|
```

### 4. Visualization Recommendations
Based on the data, suggest appropriate charts:
- Distribution → Histogram / KDE
- Comparison → Bar chart / Box plot
- Correlation → Scatter plot / Heatmap
- Time series → Line chart
- Composition → Pie chart / Stacked bar
- Geographic → Map / Choropleth

### 5. Predictive Insights
If enough data exists:
- Suggest potential ML models for prediction tasks
- Identify target variable candidates
- Recommend feature engineering strategies
- Estimate achievable accuracy range

### 6. Actionable Summary
- Top 3-5 key findings
- Recommended next steps
- Data quality issues to address before modeling

## Tools Integration
- Use **SQLite MCP** for SQL-based analysis on large datasets
- Use **Context7** for library documentation (pandas, numpy, scikit-learn)
- Use **Sequential Thinking** for complex multi-step analysis
