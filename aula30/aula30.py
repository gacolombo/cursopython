"""
Funcoes - def em Python (Parte 1)
"""


def saudacao(msg='Ola', nome='usuario'):
    nome = nome.replace('e', '3')
    print(msg, nome)


saudacao(nome='ze do caixao')
saudacao('bom dia', 'alunos')
saudacao()
saudacao(nome='roberto', msg='boa tarde')
saudacao(msg='boa noite')