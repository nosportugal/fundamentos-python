
#lista_numero = [1, 2, 44, 1, 3]
#print(type(lista_numero))

#for numero in lista_numero:
#    print(numero)

# lista_numero[0] = 10
# print(lista_numero)
# print(len(lista_numero), lista_numero[-1])

# lista_numero.sort()
# lista_numero.reverse()
# print(lista_numero)

#lista_numero.append(55)
# lista_numero.insert(0, 55)
# a = lista_numero.pop(3)
# lista_numero.remove(1)
# lista_numero.clear()
# print(a)
# print(lista_numero)
# nova_lista = lista_numero.copy()
# nova_lista = lista_numero
# print(nova_lista)

# lista = [10, "rafael", True, [10, 4, 5]]
# print(lista)


# lista = [
#     [2, 10, 10],
#     [10, 10, 10],
#     [10, 10, 10],
# ]
# print(lista[0][0])

# lista_numero = []
# for numero in range(1, 11):
#     print(lista_numero)
#     if numero % 2 == 0:
#       lista_numero.append(numero)

# print(lista_numero)

# lista_numero = [numero for numero in [10, 20, 30, 2, 4] if numero % 2 == 0]
# print(lista_numero)
# lista_numero = [1, 2, 3, 4]
# for indice, numero in enumerate(lista_numero):
#     lista_numero[indice] = numero * 2

# print(lista_numero)


# tuplas_numeros = (10, 20, 30)
# print(type(tuplas_numeros))
# tuplas_numeros[0] = 10

# lista_numero = [numero if numero % 2 == 0 else 0 for numero in [10, 20, 30, 2, 4]]

# lista = [10, 20, 40]

# tupla = (10, 20, 40)

# print(type(lista), type(tupla))

# print(tupla[0])
# tupla[0] = 100

# pessoa = {
#     "nome": "José",
#     "sobrenome": "Lisboa",
#     "idade": 30
# }


# nome = pessoa["nome"]


# endereco = pessoa.get("idade")
# print(endereco)

# pessoa = {
#     "nome": "José",
#     "sobrenome": "Lisboa",
#     "idade": 30,
#     "localizacao": {
#         "cidade": "Porto",
#         "pais": "Portugal"
#     }
# }


# nome = pessoa["nome"]


# cidade = pessoa.get("localizacao").get("cidade")
# print(cidade)

# pessoa2 = {
#     "nome": "José",
#     "sobrenome": "Lisboa",
#     "idade": 30
# }

# print("Localizacao:", pessoa2.get("localizacao"))
# cidade = pessoa2.get("localizacao", {}).get("cidade", "Lisboa")
# print(cidade)


# pessoa = {
#     "nome": "José",
#     "sobrenome": "Lisboa",
#     "localizacao": {
#         "cidade": "Porto",
#         "pais": "Portugal"
#     }
# }
# print(pessoa)
# pessoa["idade"] = 30
# print(pessoa)
# pessoa["idade"] = 60
# print(pessoa)

# del pessoa["idade"]
# print(pessoa)

# print(pessoa.pop("sobrenome", "sobrenome não existe"))
# print(pessoa)


calculadura = {
    "soma": lambda x, y: x + y,
    "subtracao": lambda x, y: x - y,
    #"multiplicacao": lambda x, y: x * y
}

soma = calculadura["soma"](10, 20)
subtracao = calculadura["subtracao"](20, 10)
print(soma)
print(subtracao)

if calculadura.get("multiplicacao"):
    multiplicacao = calculadura.get("multiplicacao")(5, 5)
    print(multiplicacao)

try:
    calculadura["multiplicacao"](5, 5)
except KeyError:
    print("nao foi possivel fazer a multiplicacao")

