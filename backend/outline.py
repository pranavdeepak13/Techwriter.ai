from backend.utils import run_llama2

class Outline:
    def generate(self, topic: str) -> str:
        prompt = f"Generate a detailed academic blog outline (Abstract, Introduction, Sections, Conclusion) on: {topic}"
        return run_llama2(prompt)
