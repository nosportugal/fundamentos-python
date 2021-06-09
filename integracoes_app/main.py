from jsonbin import create_pessoa
from telegram import send_message

pessoa = {
    "nome": "Rafael",
    "sobrenome": "Galleani"
}

status, content = create_pessoa(pessoa)
id_pessoa = content.get("metadata").get("id")
print(id_pessoa)

status_telegram, content_telegram = send_message(id_pessoa)
print(status_telegram)
print(content_telegram)


# {'record': {'nome': 'Rafael', 'sobrenome': 'Galleani'},
#  'metadata': {'id': '60bfa09d4d024768b8f364cd', 'createdAt': '2021-06-08T16:53:49.394Z', 'private': True}}
