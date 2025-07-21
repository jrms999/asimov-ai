
def parse_intent(message: str) -> dict:
    # Placeholder - ideally uses AI
    if "kill" in message or "deepfake" in message:
        return {"intent": "malicious", "risk": "harm", "content": message}
    if "leak" in message:
        return {"intent": "data_leak", "risk": "reputation", "content": message}
    return {"intent": "benign", "risk": "none", "content": message}
