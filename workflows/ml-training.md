---
name: ML Training
description: "End-to-end workflow for training machine learning predictive models."
trigger: "/ml-training"
---

# ML Training Workflow

## Step 1: Define & Engineer
- Define target variable, success metrics (Accuracy, F1, RMSE), and data constraints.
- Apply PCA, encode categories, scale features, and split (Train/Val/Test).

## Step 2: Train & Tune
- Select baseline models (Random Forest, XGBoost). Run python training scripts.
- Apply cross-validation, grid/random search, log configurations, and select the best model.

## Step 3: Evaluate & Export
- Evaluate against Test set, generate confusion matrix / residual plots.
- Export weights (`.pkl`/`.onnx`) and output inference script.

## Tools
- **Math/Calculation**: Calculate performance metrics.
- **Context7**: Look up `scikit-learn`, `pytorch`, `tensorflow` docs.
- **Memory MCP**: Store configurations and metrics across training runs.
- **Python**: Execute model training pipelines.
