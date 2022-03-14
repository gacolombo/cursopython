"""
Desempacotamento de listas em Python
"""
lista = ['Paulo', 'Luciana', 'Lucas', 1, 2, 3, 4, 5, 6, 7, 8, 9]

n1, n2, n3, *lista2, ultimo = lista

print(ultimo)
