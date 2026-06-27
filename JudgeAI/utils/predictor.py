import joblib

from utils.text_preprocessor import clean_text

# Load trained model
judgeai_model = joblib.load("models/judgeai_model.pkl")

# Load TF-IDF vectorizer
tfidf_vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


def predict_case(judgment_text):
    """
    Predict legal judgment outcome.
    """

    # Step 1 - Clean text
    cleaned_text = clean_text(judgment_text)

    # Step 2 - Convert to TF-IDF vector
    transformed_text = tfidf_vectorizer.transform([cleaned_text])

    # Step 3 - Predict
    prediction = judgeai_model.predict(transformed_text)[0]

    # Step 4 - Confidence Score
    confidence = judgeai_model.predict_proba(transformed_text).max() * 100

    return prediction, confidence


