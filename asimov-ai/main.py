"""A deliberately narrow rule-based message classifier demo."""
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator

from rules_engine import evaluate_message
from nlp_parser import parse_intent

app = FastAPI(title="Asimov rules demo")


class AnalyzeRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    sender: str = Field(min_length=1, max_length=100)

    @field_validator("message", mode="before")
    @classmethod
    def trim_message(cls, value):
        return value.strip() if isinstance(value, str) else value


@app.exception_handler(RequestValidationError)
async def validation_error_without_input(request: Request, exc: RequestValidationError):
    errors = [{key: value for key, value in error.items() if key != "input"}
              for error in exc.errors()]
    return JSONResponse(status_code=422, content={"detail": errors})


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    intent = parse_intent(request.message)
    decision = evaluate_message(intent, request.sender)
    # Never echo the original message. No request body is written to a log here.
    return {"decision": decision["action"], "reason": decision["reason"]}
