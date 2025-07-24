

from agents.ParagraphExtractor.main import ParagraphExtractorAgent
from agents.PreProcessor.main import PreprocessorAgent
from agents.Stats.main import StatsAgent
from agents.Classifier.bert_classifier import BERTClassifierAgent

if __name__ == "__main__":
    agent = ParagraphExtractorAgent()
    paragraphs = agent.run("/Users/shikhar_new/Desktop/AEC_Project/trial_paper.pdf")
    
    cleaned_paragraphs = PreprocessorAgent().run(paragraphs)

    classifier = BERTClassifierAgent(model_type='nb')
    classifier.train("/Users/shikhar_new/Desktop/AEC_Project/agents/Classifier/data/training.csv")

    classified_paragraphs = [
        {"sentence": sent, "label": classifier.classify(sent)}
        for sent in cleaned_paragraphs
    ]
    print(classified_paragraphs)

#svm=nb~=10 percent critical/descriptive ratio
