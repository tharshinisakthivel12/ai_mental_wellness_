import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("emotion_dataset_csv/train.csv")

print(df['category'].unique())

# ✅ Keep only main emotions
df = df[df['category'].isin([
    'anger', 'joy', 'sadness', 'fear', 'love', 'surprise'
])]

# ✅ Clean data
df = df.dropna(subset=['cleaned_text', 'category'])
df = df[df['cleaned_text'].str.strip() != ""]

# ✅ Safe sampling
df = df.sample(min(10000, len(df)))

# Features
X = df['cleaned_text']
y = df['category']

# Vectorizer
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_vec, y)

# Save
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("✅ Model trained successfully!")