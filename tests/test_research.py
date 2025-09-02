from backend.research import Research

def test_research(monkeypatch):
    r = Research()

    def fake_wiki(*a, **kw): return {"extract": "Wiki summary"}
    def fake_arxiv(*a, **kw):
        return type("obj", (), {"content": b"<feed><entry><title>AI Paper</title></entry></feed>"})

    monkeypatch.setattr("requests.get", lambda *a, **kw: fake_arxiv())

    result = r.gather("AI")
    assert "arxiv" in result
    assert "wikipedia" in result
