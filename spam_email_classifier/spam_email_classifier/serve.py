from fastapi import FastAPI
import joblib

app = FastAPI()

# Load model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "Spam Email Classifier API"}

@app.post("/predict")
def predict(text: str):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return {"text": text, "prediction": prediction}
