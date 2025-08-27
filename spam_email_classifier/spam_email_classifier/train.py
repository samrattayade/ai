import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import mlflow

# Load dataset
df = pd.read_csv("spam.csv")

X = df["text"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluation
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# Save model & vectorizer
joblib.dump(model, "spam_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# Log with MLflow
with mlflow.start_run():
    mlflow.log_params({"model": "LogisticRegression"})
    mlflow.sklearn.log_model(model, "model")
