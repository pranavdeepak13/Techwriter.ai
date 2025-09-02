import re

class Evaluator:
    def evaluate(self, draft: str):
        checks = {
            "abstract": "Abstract" in draft,
            "conclusion": "Conclusion" in draft,
            "code": "```python" in draft,
            "length": len(draft.split()) > 300,
        }
        score = sum(checks.values()) / len(checks)
        return {"checks": checks, "score": score}
