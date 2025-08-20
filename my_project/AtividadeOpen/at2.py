variavel = input("digita ai\n").strip().lower()
variavel2 = input("qual caractere tu quer contar?(pode ser mais de 1)\n").strip().lower()

with open("at2.txt", "w") as aas:
    aas.write(variavel)

aaaa = open("at2.txt", "r")
conteudo = aaaa.read()

contagem = 0

for caractere in conteudo:
    if caractere in variavel2:
        contagem += 1

print(f"""na frase '{variavel}' o(s) caractere(s): [{variavel2}]  aparece(m): {contagem} vez(es)""")
