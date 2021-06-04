nome = "José"
sobrenome = "Lisboa"
idade = 10
#nome_completo = nome + " " + sobrenome
#print(nome_completo)

# nome_completo = "{} {} tem {} anos".format(nome, sobrenome, idade)
# print(nome_completo)

#nome_completo = "{0} {2} tem {1} anos".format(nome, idade, sobrenome)
#print(nome_completo)

#nome_completo = "{nome} {sobronome} tem {idade} anos".format(nome=nome, idade=idade, sobronome=sobrenome)
#print(nome_completo)
''
nome_completo = f"{nome} {sobrenome} tem {idade} anos"
#print(nome_completo)
print(f"{nome} {sobrenome} tem {idade} anos")

print(len(nome_completo))
