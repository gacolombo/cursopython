"""
For / Else em Python
"""
variavel = ['joao', 'gabriel', 'maria', 'luiz']
condicao = False

for valor in variavel:
    if valor.startswith('z'):
        condicao = True

if condicao:
    print('Existe uma palavra que comeca com z')
else:
    print('nenhuma palavra comeca com z')