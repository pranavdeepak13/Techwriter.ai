import subprocess
from monitoring.logger import log_error

OLLAMA_MODEL = "llama2"

def run_llama2(prompt: str) -> str:
    """
    Run a prompt against local Ollama LLaMA2 model.
    Requires: ollama serve + ollama pull llama2
    """
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt,         
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            log_error(f"Ollama error (code {result.returncode}): {result.stderr.strip()}")
            raise RuntimeError(f"Ollama failed: {result.stderr.strip()}")
        return result.stdout.strip()
    except FileNotFoundError:
        log_error("Ollama binary not found. Install via `brew install ollama` ")
        raise
    except Exception as e:
        log_error(f"Unexpected Ollama error: {str(e)}")
        raise
