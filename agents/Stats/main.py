from collections import Counter

class StatsAgent:
    def run(self, labeled_sentences):
        label_counts = Counter(label for _, label in labeled_sentences)
        total = sum(label_counts.values())

        ratios = {
            label: round((count / total) * 100, 2)
            for label, count in label_counts.items()
        }

        return {
            "counts": dict(label_counts),
            "ratios": ratios,
            "total": total
        }
