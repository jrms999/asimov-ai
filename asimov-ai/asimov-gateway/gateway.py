
import requests
import yaml
import os

def load_config():
    with open("asimov-gateway/config.yaml", "r") as f:
        return yaml.safe_load(f)

def load_credentials():
    token = os.environ.get("ASIMOV_ACCESS_TOKEN")
    if not token:
        raise RuntimeError("Set ASIMOV_ACCESS_TOKEN for a trusted local target")
    return {"access_token": token}

def ping_ai_bot(url):
    try:
        response = requests.get(f"{url}/status", timeout=2)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def request_shell_access(url, token):
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "requestor": "Asimov AI",
        "purpose": "Ethics Audit & Dialogue",
        "access_type": "read-only",
        "valid_for": "1h"
    }
    try:
        response = requests.post(f"{url}/access-request", json=data, headers=headers, timeout=2)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def main():
    config = load_config()
    creds = load_credentials()
    for target in config["targets"]:
        print(f"--- Communicating with {target} ---")
        print("Status:", ping_ai_bot(target))
        print("Access Request:", request_shell_access(target, creds["access_token"]))

if __name__ == "__main__":
    main()
