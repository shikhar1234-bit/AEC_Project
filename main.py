# # main.py

# from agents.extractor import ParagraphExtractorAgent
# from agents.preprocessor import PreprocessorAgent
# from agents.classifier import ClassifierAgent
# from agents.stats_agent import StatsAgent
# from agents.synthesis_agent import SynthesisAgent
# from agents.report_generator import ReportGenerator

# def main(file_path):
#     # 1. Extract paragraphs/sentences
#     paragraphs = ParagraphExtractorAgent().run(file_path)

#     # 2. Preprocess (clean text)
#     cleaned = PreprocessorAgent().run(paragraphs)

#     # 3. Classify each sentence
#     labeled = ClassifierAgent().run(cleaned)

#     # 4. Get critical/descriptive stats
#     stats = StatsAgent().run(labeled)

#     # 5. Summarize findings
#     summary = SynthesisAgent().run(labeled)

#     # 6. Generate report
#     ReportGenerator().run(labeled, stats, summary)

# if __name__ == "__main__":
#     main("data/raw/sample_paper.pdf")


# test_extractor.py

from agents.ParagraphExtractor.main import ParagraphExtractorAgent
from agents.PreProcessor.main import PreprocessorAgent
from agents.Classifier.main import ClassifierAgent
from agents.Stats.main import StatsAgent



if __name__ == "__main__":
    agent = ParagraphExtractorAgent()
    paragraphs = agent.run("/Users/shikhar_new/Desktop/AEC_Project/trial_paper.pdf")
    cleaned_paragraphs=PreprocessorAgent().run(paragraphs)
    classified_paragraphs=ClassifierAgent().run(cleaned_paragraphs)
    stats = StatsAgent().run(classified_paragraphs)
    print(stats)

    

    # for i, p in enumerate(classified_paragraphs):
    #     print(f"\n--- Paragraph {i+1} ---\n{p}")
