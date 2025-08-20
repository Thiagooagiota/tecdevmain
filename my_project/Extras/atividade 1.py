while True:
    
    nomeAluno = input("digite seu nome \n")

    nota1 =float(input("digite a nota1 \n"))
    nota2 = float(input("digite a nota2 \n"))
    nota3 = float(input("digite a nota3 \n"))
    nota4 = float(input("digite a nota4 \n"))

    soma = nota1 + nota2 + nota3 + nota4
    media = round(soma / 4)

    if media < 0 or media > 10:
        print (f"""
invalido, repita o processo""")
    elif media <= 2 and media >= 0:
        print(print (f"""
{nomeAluno}

sua nota é:
{media}

VOCÊ REPROVOU"""))
    elif media > 2 and media <= 5:
        print(print (f"""
{nomeAluno}

sua nota é:
{media}

VOCÊ VAI PARA A RECUPERAÇÃO"""))
        
    elif media > 5 and media <= 10:
        print (f"""
{nomeAluno}

sua nota é:
{media}

VOCÊ PASSOU""")
