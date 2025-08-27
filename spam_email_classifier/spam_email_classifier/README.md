# Spam Email Classifier
Traditional ML pipeline using TF‑IDF + Logistic Regression. Includes experiment tracking and model evaluation dashboard.

## Features
- Data preprocessing with TF‑IDF
- Logistic Regression classifier
- Experiment tracking using MLflow
- Evaluation dashboard with accuracy, precision, recall, F1-score
- FastAPI model serving

## Installation
```bash
pip install -r requirements.txt
```

## Training
```bash
python train.py
```

## Serving the model
```bash
uvicorn serve:app --reload
```

## Dataset
Sample dataset: spam.csv (label, text)
