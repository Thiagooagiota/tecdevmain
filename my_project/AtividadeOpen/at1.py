with open("at1.txt", "w", encoding= "utf-8") as atividade:
    atividade.write("linguiça")

arquivo = open("at1.txt", "r", encoding= "utf-8")
conteudo = arquivo.read()
print("\n",conteudo,"\n")

vogais = 0

for vogal in conteudo:
    if vogal in "aeiou":
        vogais += 1

print(f"o conteudo tem {vogais} vogais")