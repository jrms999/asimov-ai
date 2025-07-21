
from fastapi import FastAPI, Request
from rules_engine import evaluate_message
from nlp_parser import parse_intent

app = FastAPI()

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    message = data.get("message")
    sender = data.get("sender")

    intent = parse_intent(message)
    decision = evaluate_message(intent, sender)

    return {"decision": decision["action"], "reason": decision["reason"]}
