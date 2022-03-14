"""
Manipulando strings  - Aula 18
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funcoes built-in len, abs, type, print, etc...
Essas funcoes podem ser usadas diretamente em cada tipo.

Voce pode conferir isso em:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""

texto = 'Python_<3'
indice = 0

for letras in texto:
    print(f'{letras} tem o indice: {indice}! :D')
    indice = indice + 1
    