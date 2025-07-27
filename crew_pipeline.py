from crewai import Agent, Task, Crew
from agents.ParagraphExtractor.main import ParagraphExtractorAgent
from agents.PreProcessor.main import PreprocessorAgent
from agents.Stats.main import StatsAgent
from agents.Classifier.bert_classifier import BERTClassifierAgent
from pydantic import PrivateAttr


# Define Agent Wrappers for CrewAI
class ParagraphExtractorWrapper(Agent):
    def __init__(self, **kwargs):
        kwargs['llm'] = None
        kwargs['verbose'] = False
        kwargs['allow_llm'] = False 
        super().__init__(**kwargs)

    def run(self, input_file: str):
        agent = ParagraphExtractorAgent()
        return agent.run(input_file)

# class PreprocessorWrapper(Agent):


#     def run(self, paragraphs):
#         return PreprocessorAgent().run(paragraphs)

# class ClassifierWrapper(Agent):
#     _model_agent: BERTClassifierAgent = PrivateAttr()

#     def __init__(self, model_type='svm',**kwargs):
#         super().__init__(**kwargs)
#         self._model_agent = BERTClassifierAgent(model_type=model_type)
#         self._model_agent.train("/Users/shikhar_new/Desktop/AEC_Project/agents/Classifier/data/training.csv")

#     def run(self, cleaned_paragraphs):
#         return [(p, self.model_agent.classify(p)) for p in cleaned_paragraphs]

# class StatsWrapper(Agent):
    def run(self, classified_paragraphs):
        return StatsAgent().run(classified_paragraphs)

# Input PDF
pdf_path = "/Users/shikhar_new/Desktop/AEC_Project/trial_paper.pdf"

# Instantiate agents
extractor_agent = ParagraphExtractorWrapper(
    name="Paragraph Extractor",
    role="PDF Parser",
    goal="Extract meaningful paragraphs from academic papers",
    backstory="An expert in parsing and extracting structured content from research PDFs.",
    llm=None
)

# preprocessor_agent = PreprocessorWrapper(
#     name="Preprocessor",
#     role="Text Cleaner",
#     goal="Clean and normalize text for analysis",
#     backstory="Specializes in cleaning raw text and preparing it for downstream processing."
# )

# classifier_agent = ClassifierWrapper(
#     name="SVM Classifier",
#     role="Paragraph Classifier",
#     goal="Classify paragraphs as critical or descriptive",
#     backstory="A machine learning expert that classifies text using SVM.",
#     model_type="svm"
# )

# stats_agent = StatsWrapper(
#     name="Statistics Generator",
#     role="Stats Generator",
#     goal="Analyze classification results",
#     backstory="Crunches numbers to provide summaries of classified content."
# )

# Define tasks
extract_task = Task(
    name="extract_task",  # ← REQUIRED!
    description="Extract paragraphs from PDF",
    expected_output="List of paragraphs",
    agent=extractor_agent
)

# preprocess_task = Task(
#     description="Clean and preprocess extracted paragraphs",
#     expected_output="List of cleaned paragraphs",
#     agent=preprocessor_agent,
#     context=[extract_task]
# )

# classify_task = Task(
#     description="Classify paragraphs as critical or descriptive using SVM",
#     expected_output="List of (paragraph, label)",
#     agent=classifier_agent,
#     context=[preprocess_task]
# )

# stats_task = Task(
#     description="Generate statistics on classified paragraphs",
#     expected_output="Summary statistics of classifications",
#     agent=stats_agent,
#     context=[classify_task]
# )

# Assemble Crew
crew = Crew(
    agents=[extractor_agent],
    tasks=[extract_task],
    verbose=True,
    llm=None   # ← Add this line!

)

# Execute pipeline
final_output = crew.kickoff(inputs={extract_task.name: pdf_path})
print("\nFinal Output:\n", final_output)
