# 🧠 Multi-Agent Research Paper Analyzer

This project implements a modular **multi-agent pipeline** to analyze academic research papers in PDF format. Each agent performs a specific step in the process — from extracting raw text to generating high-level insights.

The system follows a CrewAI-style architecture but can also run independently without LLMs or OpenAI API.

---

## 🚀 What It Does

1. **Extracts** paragraphs from a research paper (PDF)
2. **Preprocesses** the raw text (cleaning, normalizing)
3. **Classifies** each paragraph as `critical` or `descriptive`
4. **Analyzes** statistics such as ratio, frequency, etc.

---

## 🧠 Agents in the Pipeline

### 1. **ParagraphExtractor Agent**
- **Role:** Reads a PDF and extracts paragraphs using `PyMuPDF`.
- **Input:** Path to `.pdf` file
- **Output:** List of raw paragraphs (`List[str]`)

### 2. **PreProcessor Agent**
- **Role:** Cleans, trims, and normalizes text (e.g., removes noise).
- **Input:** List of raw paragraphs
- **Output:** List of cleaned paragraphs (`List[str]`)

### 3. **Classifier Agent**
- **Role:** Classifies each paragraph as `critical` or `descriptive`
- **Model:** SVM or NB using  BERT (local)
- **Input:** Cleaned paragraph list
- **Output:** List of tuples `(paragraph, label)`

### 4. **StatsAgent**
- **Role:** Computes statistics — percentage of critical vs descriptive content
- **Input:** Labeled paragraph list
- **Output:** Dictionary or summary report

---

## 🧩 Folder Structure

