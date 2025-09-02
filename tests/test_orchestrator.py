from backend.orchestrator import Orchestrator

class DummyResearch: 
    def gather(self, t): return {"arxiv": ["a"], "wikipedia": "b"}
class DummyOutline: 
    def generate(self, t): return "Outline"
class DummyWriter: 
    def expand(self, o, c, f=None, d=None): return "Draft"
class DummyReviewer: 
    def validate_code(self, d): return d
class DummyFormatter: 
    def format(self, d, c): return "FinalMD"
class DummyEvaluator: 
    def evaluate(self, d): return {"score": 1.0}

def test_orchestrator():
    o = Orchestrator()
    o.research, o.outline, o.writer = DummyResearch(), DummyOutline(), DummyWriter()
    o.reviewer, o.formatter, o.evaluator = DummyReviewer(), DummyFormatter(), DummyEvaluator()
    result = o.run_initial("AI")
    assert "draft" in result
    assert "evaluation" in result
