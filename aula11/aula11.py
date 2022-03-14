"""
Operadores Relacionais - Aula 11
== > >= < <= !=
"""
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
if idade >= 20 and idade <= 30:
    print(f'Parabens, {nome}! Voce tem direito ao emprestimo')
else:
    print(f'Desculpe-nos, {nome}. Voce nao tem direito ao emprestimo.')