from backend.outline import Outline

class DummyLLM:
    def invoke(self, prompt): return type("obj", (), {"content": "Outline Content"})

def test_outline(monkeypatch):
    o = Outline()
    o.llm = DummyLLM()
    result = o.generate("AI")
    assert "Outline" in result
