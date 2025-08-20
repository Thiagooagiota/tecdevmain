infos = {"nome:": 19, "sexo:": "desconheço", "altura:": "1,70", "endereço:": "aquela rua la"}
print(infos)
print(infos.keys())
print(infos.items())
print(infos.values())

for chave in infos:
    print(chave, infos[chave])
for chave, valor in infos.items():
    print(chave, valor)
