---
name: ML Training
description: "End-to-end workflow for training machine learning predictive models."
trigger: "/ml-training"
---

# ML Training Workflow

## Step 1: Problem Definition
- Identify target variable (regression vs classification)
- Define success metrics (Accuracy, F1-Score, RMSE, etc.)
- Understand dataset constraints

## Step 2: Feature Engineering
- Perform dimensionality reduction (PCA) if necessary
- Encode categorical variables
- Scale and normalize features
- Split into Training, Validation, and Test sets

## Step 3: Model Selection & Training
- Select baseline models (Random Forest, Logistic Regression, XGBoost, etc.)
- Use the **Python Execution Environment** (via generated scripts) to train models.
- Apply cross-validation

## Step 4: Hyperparameter Tuning
- Perform Grid Search or Random Search
- Log metrics for each configuration
- Select best performing model

## Step 5: Evaluation & Export
- Evaluate against Test set
- Generate confusion matrix / residual plots
- Export trained model weights (e.g., `.pkl` or `.onnx`)
- Output inference script

## Tools
- **Math/Calculation**: Calculate performance benchmarks
- **Context7**: Look up `scikit-learn`, `pytorch`, `tensorflow` docs
- **Memory MCP**: Store hyperparameter results across runs
- **Python**: Run the actual training pipelines
