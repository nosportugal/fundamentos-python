from jsonbin import create_pessoa
from telegram import send_message

pessoa = {
    "nome": "Jose",
    "sobrenome": "Lisboa"
}

status, content = create_pessoa(pessoa)
id_pessoa = content.get("metadata").get("id")
print(id_pessoa)

chat_id = 123 # alterar aqui o chat id
status_telegram, content_telegram = send_message(id_pessoa, chat_id)
print(status_telegram)
print(content_telegram)


