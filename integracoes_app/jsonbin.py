from urllib.parse import urljoin
import requests
import os

URL = "https://api.jsonbin.io/v3/b/"

TOKEN = os.environ["TOKEN_JSONBIN"]


def get_pessoa(id_pessoa):
    url_pessoa = urljoin(URL, id_pessoa)
    headers = {"X-Master-Key": TOKEN}
    # response = requests.get(url, auth=(user, password))
    # response = requests.get(url, auth=(os.environ["USER_JSONBIN"], os.environ["PASSWORD_JSONBIN"]))
    response = requests.get(url_pessoa, headers=headers)
    return response.json()


def put_pessoa(id_pessoa):
    # url = "https://api.jsonbin.io/v3/b/<id_pessoa>"
    url_pessoa = urljoin(URL, id_pessoa)
    response = requests.put(url_pessoa, json=pessoa)
    print(response.text)
    return response.status_code, response.json()


def delete_pessoa(id_pessoa):
    # url = "https://api.jsonbin.io/v3/b/<id_pessoa>"
    url_pessoa = urljoin(URL, id_pessoa)
    headers = {"X-Master-Key": TOKEN}
    response = requests.delete(url_pessoa, headers=headers)
    return response.status_code, response.json()


def create_pessoa(pessoa):
    headers = {"X-Master-Key": TOKEN}
    response = requests.post(URL, json=pessoa, headers=headers)
    return response.status_code, response.json()


if __name__ == "__main__":
    # pessoa = get_pessoa("<id_pessoa>")
    # print(pessoa)
    pessoa = {"nome": "Rafael", "sobrenome": "Galleani"}
    # status, content = put_pessoa(pessoa)
    # status, content = delete_pessoa()
    status, content = create_pessoa(pessoa)
    print(status, content)
