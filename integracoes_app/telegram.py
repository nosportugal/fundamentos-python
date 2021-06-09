from urllib.parse import urljoin
import requests
import os

TOKEN = os.environ["TOKEN_JSONBIN"]
URL = f"https://api.telegram.org/bot{TOKEN}/"


def send_message(text):
    url = urljoin(URL, "sendMessage")
    data = {"chat_id": "159062336", "text": text}
    response = requests.post(url, json=data)
    return response.status_code, response.json()


if __name__ == "__main__":
    send_message("Olá")
