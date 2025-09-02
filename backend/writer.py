from backend.utils import run_llama2

class Writer:
    def expand(self, outline: str, citations: dict, feedback: str = None, prev_draft: str = None) -> str:
        prompt = f"""
        Expand this outline into a full blog post with Abstract, Introduction, explanations,
        runnable Python code snippets, and references.

        Outline: {outline}
        Citations: {citations}
        """
        if feedback:
            prompt += f"\nIncorporate this feedback: {feedback}"
        if prev_draft:
            prompt += f"\nImprove upon this previous draft: {prev_draft[:1500]}"
        return run_llama2(prompt)
