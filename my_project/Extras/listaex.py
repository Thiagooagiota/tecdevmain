lista = [1, 2, 3, 4, 5]
print(lista)
# Adicionando elementos com .append(), .insert() e .extend()
lista.append(6) # adiciona 6 ao final da lista
print(lista)
lista.insert(0, 0) # insere 0 na posição 0
print(lista)
lista.extend([7, 8, 9]) # adiciona os elementos 7, 8, 9 ao final da lista
print(lista)

# Removendo elementos com .remove(), .pop() e .clear()
lista.remove(5) # remove o elemento 5
print(lista)
elemento_removido = lista.pop(2) # remove o elemento na posição 2 e retorna o valor removido
print(lista)
print(elemento_removido)
lista.clear() # limpa a lista completamente
print(lista)
