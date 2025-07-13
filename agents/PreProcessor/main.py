import re
import string

class PreprocessorAgent:
    def __init__(self, remove_stopwords=True):
        self.remove_stopwords = remove_stopwords
        self.stopwords = set(self._load_stopwords()) if remove_stopwords else set()

    def run(self, sentences):
        cleaned = [self._clean_text(s) for s in sentences]
        return cleaned

    def _clean_text(self, text):
        text = text.lower()
        text = re.sub(r"\d+", "", text)
        text = text.translate(str.maketrans("", "", string.punctuation))
        tokens = text.split()
        if self.remove_stopwords:
            tokens = [word for word in tokens if word not in self.stopwords]
        return " ".join(tokens)

    def _load_stopwords(self):
        return [
            "a", "an", "the", "and", "or", "but", "if", "then", "is", "are", "was", "were", "be",
            "has", "had", "have", "in", "on", "for", "with", "as", "by", "to", "of", "at", "this",
            "that", "these", "those", "it", "its", "from", "they", "them", "not", "no", "yes"
        ]
