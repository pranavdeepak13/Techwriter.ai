from dotenv import load_dotenv
load_dotenv()   # ensure .env is loaded early

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.orchestrator import Orchestrator

app = FastAPI(title="AI Blog Writer (LLaMA2)", version="1.0.0")

orchestrator = Orchestrator()

class GenerateRequest(BaseModel):
    topic: str

class FeedbackRequest(BaseModel):
    feedback: str

@app.get("/health")
def health():
    return {"status": "ok", "mode": "Ollama (llama2)"}

@app.post("/generate")
def generate(req: GenerateRequest):
    topic = req.topic.strip()
    if len(topic.split()) < 3:
        raise HTTPException(status_code=400, detail="Please provide a more specific topic (min 3 words).")
    result = orchestrator.run_initial(topic)
    return result

@app.post("/feedback")
def feedback(req: FeedbackRequest):
    if orchestrator.latest_draft is None:
        raise HTTPException(status_code=400, detail="No draft exists yet. Call /generate first.")
    result = orchestrator.redraft(req.feedback)
    return result

@app.post("/approve")
def approve():
    if orchestrator.latest_draft is None:
        raise HTTPException(status_code=400, detail="No draft to approve.")
    with open("output/blog_draft.md", "w") as f:
        f.write(orchestrator.latest_draft)
    return {"status": "approved", "file": "output/blog_draft.md"}
