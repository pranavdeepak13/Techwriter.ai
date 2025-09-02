from backend.formatter import Formatter

def test_formatter_format():
    f = Formatter()
    draft = "This is a draft"
    citations = {"arxiv": ["Paper"]}
    md = f.format(draft, citations)
    assert "# Medium Blog Draft" in md
    assert "References" in md
