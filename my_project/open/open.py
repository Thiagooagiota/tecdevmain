with open("exemplo.txt", "w") as teste:
    teste.write("testando\n")
    teste.write("\ntestando")

with open("exemplo.txt", "a") as teste:
    teste.write("\ntestando a\n")


arquivo = open("exemplo.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()