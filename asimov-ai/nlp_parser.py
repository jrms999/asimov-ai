"""Keyword matching, not NLP or semantic understanding."""
import re


def parse_intent(message: str) -> dict:
    words = set(re.findall(r"\b[a-z]+\b", message.casefold()))
    if words & {"kill", "deepfake"}:
        return {"intent": "flagged_keyword", "risk": "harm"}
    if "leak" in words:
        return {"intent": "flagged_keyword", "risk": "potential_disclosure"}
    if "sensitive government content" in message.casefold():
        return {"intent": "flagged_phrase", "risk": "potential_disclosure"}
    return {"intent": "no_match", "risk": "none"}
