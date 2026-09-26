"""A deliberately narrow rule-based message classifier demo."""
from fastapi import FastAPI
from pydantic import BaseModel, Field

from rules_engine import evaluate_message
from nlp_parser import parse_intent

app = FastAPI(title="Asimov rules demo")


class AnalyzeRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    sender: str = Field(min_length=1, max_length=100)


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    intent = parse_intent(request.message)
    decision = evaluate_message(intent, request.sender)
    # Never echo the original message. No request body is written to a log here.
    return {"decision": decision["action"], "reason": decision["reason"]}
