"""
1 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada
"""


def func1(arg):
    return arg


def func2():
    return print('Eu acho que eh isso')

func1(func2())

"""
2 - Crie uma funcao1 que receba uma funcao2 como parametro e retorne o valor da
funcao2 executada. Faca a funcao1 executar duas funcoes que recebam um numero
diferente de argumentos.
"""


def mestre(*args):
    return print(f'A funcao um eh: "{args[0]}" e a dois eh: "{args[1]}"')


def soma(n1, n2):
    return f'A somatoria dos numeros eh: {n1 + n2}'


def hora(horario):
    return f'O horario de agora eh: {horario}'


mestre(soma(1, 2), hora(23))
