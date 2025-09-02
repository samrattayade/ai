# house_price_prediction.py
# End-to-End House Price Prediction (Windows-friendly, error-free)

import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, StackingRegressor

# 1) Load dataset (make sure house_prices.csv is in the same folder)
df = pd.read_csv("house_prices.csv")

# 2) Feature Engineering (example: house_age)
if "YrSold" in df.columns and "YearBuilt" in df.columns:
    df["house_age"] = df["YrSold"] - df["YearBuilt"]

# Target and features
y = df["SalePrice"]
X = df.drop("SalePrice", axis=1)

# 3) Identify numeric and categorical features
numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = X.select_dtypes(include=["object"]).columns.tolist()

# 4) Preprocessing pipelines
numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# 5) Compare models with 5-fold cross-validation (RMSE)
models = {
    "Linear Regression": LinearRegression(),
    "Ridge": Ridge(),
    "Random Forest": RandomForestRegressor(random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42)
}

print("\nCross-Validation RMSE Scores:")
for name, model in models.items():
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
    # use neg_mean_squared_error then take sqrt for RMSE
    scores = -cross_val_score(pipeline, X, y, cv=5, scoring="neg_mean_squared_error")
    rmse_scores = np.sqrt(scores)
    print(f"{name}: {rmse_scores.mean():.2f}")

# 6) Model stacking (train/test split for final evaluation)
base_models = [
    ("ridge", Ridge()),
    ("rf", RandomForestRegressor(random_state=42)),
    ("gb", GradientBoostingRegressor(random_state=42))
]

stack_model = StackingRegressor(estimators=base_models, final_estimator=LinearRegression())

stack_pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", stack_model)])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

stack_pipeline.fit(X_train, y_train)
y_pred = stack_pipeline.predict(X_test)

# RMSE calculation (always works)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"\nFinal stacked model RMSE on test set: {rmse:.2f}")
