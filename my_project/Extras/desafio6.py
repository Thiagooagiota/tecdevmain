sus = []
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
]

for i in range(len(perguntas)):
    usuario = int(input(f"""
{perguntas[i]}



1 - sim             2 - não

            """))

    sus.append(usuario)
respostas = sus.count(1)

if respostas == 2:
    print("suspeito")
elif respostas == 3 or respostas == 4:
    print("cumplice")
elif respostas == 5:
    print("assassino")
else:
    print("inocente")
