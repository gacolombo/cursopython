"""
While / Else - Aula 20
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(f'{contador}, {acumulador}')

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')
