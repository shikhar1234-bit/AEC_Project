from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import re
from collections import Counter

class ParagraphExtractorAgent:
    def run(self, pdf_path):
        text = self._extract_clean_text(pdf_path)
        sentences = self._split_into_sentences(text)
        return sentences

    def _extract_clean_text(self, pdf_path):
        page_lines = []
        line_counts = Counter()

        for page_layout in extract_pages(pdf_path):
            lines = []
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    for line in element.get_text().splitlines():
                        clean_line = line.strip()
                        if clean_line:
                            lines.append(clean_line)
                            line_counts[clean_line] += 1
            page_lines.append(lines)

        # Identify repeated lines (likely headers/footers)
        repeated_lines = {line for line, count in line_counts.items() if count > 1}

        # Rebuild cleaned full text
        full_text = ""
        for lines in page_lines:
            for line in lines:
                if (
                    line not in repeated_lines and
                    not re.match(r"^\s*(Page\s+\d+|DOI:|©|Copyright|All rights reserved)", line, re.IGNORECASE) and
                    len(line.strip()) > 20
                ):
                    full_text += line.strip() + " "

        return full_text.strip()

    def _split_into_sentences(self, text):
        text = re.sub(r'\s+', ' ', text).strip()

        protected = {
            "e.g.": "egDOT",
            "i.e.": "ieDOT",
            "Dr.": "DrDOT",
            "Mr.": "MrDOT",
            "Ms.": "MsDOT",
            "etc.": "etcDOT"
        }
        for abbr, token in protected.items():
            text = text.replace(abbr, token)

        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

        for i in range(len(sentences)):
            for abbr, token in protected.items():
                sentences[i] = sentences[i].replace(token, abbr)

        return [s.strip() for s in sentences if len(s.strip()) > 20]
