"""
For in em Python
Iterando strings com for
Funcao range(start = 0, stop, step = 1)
"""

texto = 'o rato roeu a roupa do rei de roma'
nova_string = ''

for letra in texto:
    if letra == 'r':
        nova_string = nova_string + letra.upper()
    else:
        nova_string += letra
print(nova_string)