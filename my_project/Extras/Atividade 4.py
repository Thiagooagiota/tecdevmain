nome = input("seu nome \n" )
sobrenome = input("seu sobrenome \n")

#possibilidade
# nome,sobrenome = sobrenome,nome#

#maneira correta#
aux = nome
nome = sobrenome
sobrenome = aux



print(f"seu nome e: {nome} {sobrenome}")