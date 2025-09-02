from backend.writer import Writer

class DummyLLM:
    def invoke(self, prompt): return type("obj", (), {"content": "Blog Content"})

def test_writer_expand():
    w = Writer()
    w.llm = DummyLLM()
    result = w.expand("Outline", {"arxiv": "cite"})
    assert "Blog" in result
