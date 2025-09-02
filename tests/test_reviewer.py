from backend.reviewer import Reviewer

def test_reviewer_validate_code():
    draft = """```python
print("Hello Test")
```"""
    r = Reviewer()
    result = r.validate_code(draft)
    assert isinstance(result, str)
    assert "Hello" in draft
