import os
os.makedirs("models", exist_ok=True)
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load file
df = pd.read_csv("training_data.csv")

X_texts = df["Text"]
y_labels = df["NACE"]

# TF-IDF + Model training
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X_texts)

model = LogisticRegression(max_iter=1000)
model.fit(X, y_labels)

# Save
joblib.dump(vectorizer, "models/nace_vectorizer.pkl")
joblib.dump(model, "models/nace_model.pkl")

print("Training done & saved!")