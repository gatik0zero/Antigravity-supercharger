---
trigger: glob
globs: ["*.py", "*.ipynb", "*.csv", "*.json", "*.parquet", "*.xlsx"]
---

# Data Science & ML Rules

## Data Handling
- Always inspect data before processing: shape, dtypes, null counts, distributions
- Never modify raw data — create processed copies
- Document data transformations and their rationale
- Use consistent datetime formats (ISO 8601)
- Handle missing values explicitly (don't silently drop rows)

## Analysis
- Start with exploratory data analysis (EDA) before modeling
- Use appropriate statistical tests — don't just eyeball it
- Report confidence intervals, not just point estimates
- Visualize distributions before assuming normality
- Document assumptions made during analysis

## Machine Learning
- Split data into train/validation/test BEFORE any preprocessing
- Use cross-validation for model selection
- Track all experiments: hyperparameters, metrics, data versions
- Prefer simpler models unless complexity is justified by performance
- Always evaluate on held-out test data (never tune on test set)

## Visualization
- Every chart needs: title, labeled axes, legend (if multiple series)
- Choose appropriate chart types (bar for categories, line for time, scatter for correlation)
- Use colorblind-friendly palettes
- Keep visualizations clean — remove chartjunk
- Include data source and date in captions

## Math & Statistics
- Show your work — include formulas and intermediate steps
- Use appropriate precision (don't report 10 decimal places)
- Distinguish between correlation and causation
- Report effect sizes alongside p-values
- Use Monte Carlo simulation for complex probability problems

## IoT Data
- Handle time-series data with proper resampling
- Account for sensor noise and outliers
- Use rolling averages for smoothing
- Document sensor specifications and calibration
- Consider edge computing constraints for real-time processing
