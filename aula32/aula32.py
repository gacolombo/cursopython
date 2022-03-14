"""
funcoes (def) em python - *args *kwargs -
Aula 32 (Parte 3)
"""


def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'])
    nome = kwargs.get('nome')
    print(nome)


func(1, 2, 3, 4, 5, 6, nome='Gabriel', sobrenome='Colombo', idade='24')
