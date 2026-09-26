from fastapi.testclient import TestClient
from main import app
from nlp_parser import parse_intent
from rules_engine import evaluate_message

client = TestClient(app)


def test_benign():
    result = evaluate_message(parse_intent("hello"), "botA")
    assert result["action"] == "allow"
    assert "safety not established" in result["reason"]


def test_harm_case_and_word_boundary():
    assert evaluate_message(parse_intent("KILL"), "botA")["action"] == "block"
    assert evaluate_message(parse_intent("skill"), "botA")["action"] == "allow"


def test_disclosure():
    assert evaluate_message(parse_intent("LEAK"), "botA")["action"] == "warn"
    assert evaluate_message(parse_intent("sensitive government content"), "botA")["action"] == "warn"


def test_api_validation_and_no_echo():
    for body in ({}, {"message": "", "sender": "botA"},
                 {"message": None, "sender": "botA"},
                 {"message": "x" * 4001, "sender": "botA"}):
        assert client.post("/analyze", json=body).status_code == 422
    response = client.post("/analyze", json={"message": "LEAK private notes", "sender": "botA"})
    assert response.status_code == 200
    assert response.json()["decision"] == "warn"
    assert "private notes" not in response.text


def test_overlong_message_is_not_echoed_in_validation_error():
    secret = "sensitive-message-" * 251
    response = client.post("/analyze", json={"message": secret, "sender": "botA"})
    assert response.status_code == 422
    assert secret not in response.text
    assert all("input" not in error for error in response.json()["detail"])


def test_whitespace_only_messages_are_rejected():
    for message in ("   ", " \n\t "):
        response = client.post("/analyze", json={"message": message, "sender": "botA"})
        assert response.status_code == 422
        assert response.json()["detail"][0]["loc"] == ["body", "message"]


def test_known_false_positive_is_documented():
    # The rules cannot understand negation; this is a limit, not a passed safety guarantee.
    assert evaluate_message(parse_intent("Do not leak data"), "botA")["action"] == "warn"
