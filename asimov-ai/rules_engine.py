"""Explicit demo decisions. A keyword hit is not a safety determination."""


def evaluate_message(intent: dict, sender: str):
    risk = intent.get("risk")
    if risk == "harm":
        return {"action": "block", "reason": "Harm-related keyword matched; manual review needed"}
    if risk == "potential_disclosure":
        return {"action": "warn", "reason": "Potential disclosure keyword matched; manual review needed"}
    return {"action": "allow", "reason": "No configured keyword matched; safety not established"}
