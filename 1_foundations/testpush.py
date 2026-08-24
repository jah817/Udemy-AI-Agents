from dotenv import load_dotenv
import os
import requests

def push(message):
    print(f"Push: {message}")
    payload = {"user": pushover_user, "token": pushover_token, "message": message}
    response = requests.post(pushover_url, data=payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

load_dotenv(override=True)

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_url = "https://api.pushover.net/1/messages.json"

if pushover_user and pushover_token:
    push("This test push worked!")
else:
    push("Pushover user or token not found")