import os
import pandas as pd
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sentence_transformers import SentenceTransformer

class BERTClassifierAgent:
    def __init__(self, model_type='svm'):
        """
        model_type: 'svm' or 'nb'
        """
        self.model_type = model_type
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self.model = None

    def load_data(self, data_path):
        df = pd.read_csv(data_path)
        df = df.dropna(subset=["sentence", "label"])
        return df["sentence"].tolist(), df["label"].tolist()

    def encode_sentences(self, sentences):
        return self.encoder.encode(sentences)

    def train(self, data_path):
        X_raw, y = self.load_data(data_path)
        X_embeddings = self.encode_sentences(X_raw)

        if self.model_type == 'svm':
            self.model = SVC(kernel='linear', probability=True)
        elif self.model_type == 'nb':
            self.model = GaussianNB()
        else:
            raise ValueError("Invalid model_type. Use 'svm' or 'nb'.")

        X_train, X_test, y_train, y_test = train_test_split(X_embeddings, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def classify(self, sentence: str) -> str:
        embedding = self.encode_sentences([sentence])
        return self.model.predict(embedding)[0]

# Example usage
if __name__ == "__main__":

    svm_agent = BERTClassifierAgent(model_type='svm')
    svm_agent.train("/Users/shikhar_new/Desktop/AEC_Project/agents/Classifier/data/training.csv")
    print("Prediction (SVM):", svm_agent.classify("Our novel model increases processing speed significantly."))

    nb_agent = BERTClassifierAgent(model_type='nb')
    nb_agent.train("/Users/shikhar_new/Desktop/AEC_Project/agents/Classifier/data/training.csv")
    print("Prediction (NB):", nb_agent.classify("This section presents the literature review."))
