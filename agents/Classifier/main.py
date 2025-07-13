import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

class ClassifierAgent:
    def __init__(self, train_file="data/training.csv"):
        self.train_file = train_file
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()
        self._train_model()

    def _train_model(self):
        if not os.path.exists(self.train_file):
            raise FileNotFoundError(f"Training file not found: {self.train_file}")

        df = pd.read_csv(self.train_file)
        sentences = df["sentence"].astype(str).tolist()
        labels = df["label"].astype(str).tolist()

        X = self.vectorizer.fit_transform(sentences)
        self.model.fit(X, labels)

    def run(self, cleaned_sentences):
        X_test = self.vectorizer.transform(cleaned_sentences)
        predictions = self.model.predict(X_test)
        return list(zip(cleaned_sentences, predictions))
