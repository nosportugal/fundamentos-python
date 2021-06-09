import requests


def send_message(text):
    url = "https://api.telegram.org/bot1706760277:AAHEtNJqwY-gtXuUQTa2lHuL5Yl4CFzROdA/sendMessage"
    data = {
        "chat_id": "159062336",
        "text": text
    }
    response = requests.post(url, json=data)
    return response.status_code, response.json()

if __name__ == "__main__":
    send_message("Olá")
