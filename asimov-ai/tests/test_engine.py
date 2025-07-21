
from rules_engine import evaluate_message

def test_benign():
    result = evaluate_message({"intent": "benign", "risk": "none", "content": "hello"}, "botA")
    assert result["action"] == "allow"

def test_harm():
    result = evaluate_message({"intent": "malicious", "risk": "harm", "content": "kill"}, "botA")
    assert result["action"] == "block"

def test_sensitive():
    result = evaluate_message({"intent": "data_leak", "risk": "reputation", "content": "sensitive government content"}, "botA")
    assert result["action"] == "warn"
