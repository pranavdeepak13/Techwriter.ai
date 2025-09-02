import re, subprocess, tempfile

class Reviewer:
    def validate_code(self, draft: str) -> str:
        code_blocks = re.findall(r"```python(.*?)```", draft, re.DOTALL)
        for block in code_blocks:
            with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
                f.write(block.strip())
                f.flush()
                try:
                    subprocess.run(["python3", f.name], check=True, capture_output=True)
                except subprocess.CalledProcessError as e:
                    draft += f"\n⚠️ Code execution failed: {e}\n"
        return draft
