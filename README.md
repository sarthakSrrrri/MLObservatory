# ModelProbe

> An ML model diagnostics platform for finding, understanding, and validating problems in machine learning models.

## Overview

ModelProbe is a web-based tool that helps developers and ML engineers understand whether their machine learning models are reliable.

A user will be able to upload a dataset and trained ML model, and ModelProbe will analyze the model and its data to identify potential problems such as data quality issues, overfitting, data leakage, class imbalance, feature problems, and data drift.

The goal is not just to report a problem, but to explain:

- What is wrong?
- Why is it a problem?
- What evidence supports the diagnosis?
- What can be done to fix it?
- Did the model improve after the fix?

## Architecture

```text
React Frontend
       │
       │ HTTP API
       ▼
FastAPI Backend
       │
       ▼
ML Diagnostics Engine
       │
       ├── Data Quality
       ├── Model Evaluation
       ├── Leakage Detection
       ├── Explainability
       └── Drift Detection