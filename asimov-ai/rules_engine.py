
def evaluate_message(intent: dict, sender: str):
    # Simulate logic from Asimov’s Laws
    if "harm" in intent.get("risk", ""):
        return {"action": "block", "reason": "Violates Law 1"}
    if "sensitive government content" in intent.get("content", ""):
        return {"action": "warn", "reason": "Potential Law 4 conflict"}
    return {"action": "allow", "reason": "No violation detected"}
