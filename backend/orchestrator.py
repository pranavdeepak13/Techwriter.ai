from backend.research import Research
from backend.outline import Outline
from backend.writer import Writer
from backend.reviewer import Reviewer
from backend.formatter import Formatter
from backend.evaluator import Evaluator

class Orchestrator:
    def __init__(self):
        self.research, self.outline, self.writer = Research(), Outline(), Writer()
        self.reviewer, self.formatter, self.evaluator = Reviewer(), Formatter(), Evaluator()
        self.latest_draft, self.latest_outline, self.latest_citations = None, None, None

    def run_initial(self, topic: str):
        citations = self.research.gather(topic)
        outline = self.outline.generate(topic)
        draft = self.writer.expand(outline, citations)
        reviewed = self.reviewer.validate_code(draft)
        evaluation = self.evaluator.evaluate(reviewed)
        final_md = self.formatter.format(reviewed, citations)
        self.latest_draft, self.latest_outline, self.latest_citations = final_md, outline, citations
        return {"draft": final_md, "evaluation": evaluation}

    def redraft(self, feedback: str):
        draft = self.writer.expand(self.latest_outline, self.latest_citations, feedback, self.latest_draft)
        reviewed = self.reviewer.validate_code(draft)
        evaluation = self.evaluator.evaluate(reviewed)
        final_md = self.formatter.format(reviewed, self.latest_citations)
        self.latest_draft = final_md
        return {"draft": final_md, "evaluation": evaluation}
