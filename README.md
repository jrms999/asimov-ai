# Asimov AI — rule-based oversight experiment

**Prototype, not a dependable safety filter.** This FastAPI service classifies a message using a few explicit keywords and returns `allow`, `warn` or `block`. It does not understand intent, context, negation or real-world harm. An `allow` result means only that no configured keyword matched. The API does not log or echo the submitted message, but infrastructure logs and deployment settings require separate review.

## Run and test

```bash
cd asimov-ai
python -m venv .venv
source .venv/bin/activate
pip install fastapi uvicorn pytest httpx requests pyyaml
python -m pytest tests -q
uvicorn main:app --host 127.0.0.1 --port 8000
```

Example with fictional text:

```bash
curl -X POST http://127.0.0.1:8000/analyze -H 'Content-Type: application/json' -d '{"sender":"demo","message":"A sample message"}'
```

The API rejects blank, missing, non-string or overlong message input. Tests cover case handling, word boundaries, disclosure flags, no raw-message response, and a known false positive (`Do not leak data`). These are behaviour tests, not evidence of accurate safety classification.

The separate `asimov-gateway` experiment sends requests to configured targets. Its old committed `credentials.json` contained a placeholder; the file is removed from the current tree. The gateway now reads `ASIMOV_ACCESS_TOKEN` from the environment. Never use a real token in Git; rotate any real credential that may have been committed historically. Do not point the gateway at systems you do not administer or have permission to test.

## Next steps

- Define a versioned policy format with explicit rules, rationale and test fixtures.
- Build an evaluation set with expected outcomes, false positives and misses; report measured limitations.
- Add bounded structured decision metadata without storing message bodies, and review logging at the hosting layer.
- Obtain human review for consequential decisions. A keyword rule should not be used to enforce policy in production.
