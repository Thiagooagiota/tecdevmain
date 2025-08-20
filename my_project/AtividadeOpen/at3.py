variavel = input("digita ai\n").strip().lower()

with open("at3.txt", "w") as aas:
    aas.write(variavel)


aaaa = open("at3.txt", "r")
conteudo = aaaa.read()

resultado = conteudo

for caractere in conteudo:
    if caractere in "aeiou":
        resultado = resultado.replace(caractere,"*")
    
with open("at3-1.txt", "w") as aas:
    aas.write(conteudo)

print(f"""{resultado}""")
