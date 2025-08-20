vendas = [941, 852, 783, 714, 697, 686, 685, 
670, 631, 453, 386, 371, 294, 269, 259]
vendedores = ['Maria','José', 'Antônio', 'João', 
'Francisco', 'Ana', 'Luiz',
'Paulo', 'Carlos', 'Fernanda', 'Juliana', 
'Sandro', 'Fábio', 'Tatiane', 'Célia']

for i in range(len(vendas)):

    if vendas[i] >= 700:
        print(f"o vendedor {vendedores[i]} vendeu R${vendas[i]}")