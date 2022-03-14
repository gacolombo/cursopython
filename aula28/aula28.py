"""
Operadores ternario em Python
"""
idade = input('Qual a sua idade?')
if not idade.isnumeric():
    print('Valor invalido')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Pode acessar' if maior else 'N pode acessar'

    print(msg)