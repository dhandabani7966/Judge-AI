import os
import joblib
from utils.text_preprocessor import clean_text

# Fix: absolute path use பண்ணு
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "judgeai_model.pkl")
TFIDF_PATH = os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")

judgeai_model = joblib.load(MODEL_PATH)
tfidf_vectorizer = joblib.load(TFIDF_PATH)

def predict_case(text):
    cleaned = clean_text(text)
    features = tfidf_vectorizer.transform([cleaned])
    prediction = judgeai_model.predict(features)[0]
    confidence = judgeai_model.predict_proba(features).max() * 100
    return prediction, round(confidence, 2)
