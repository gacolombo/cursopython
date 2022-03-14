"""
Formatando valores com modificadores - Aula 17

:s - Texto (strings)
:d - Inteiros (int)
:f - Numeros de ponto flutuantes (floats)
:. (numero)f - quatidade de casas decimais (float)
:(CARACTERE) (> OU < OU ^) (quantidade) (TIPO - s, d ou f)

> - ESQUERDA
< - DIREITA
^ - CENTRO
"""

nome = 'Gabriel'
sobrenome = 'Colombo'
qualquer = 'Naju'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome, qualquer)
print(nome_formatado)

