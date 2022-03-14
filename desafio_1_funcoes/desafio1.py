"""
1 - Crie uma funcao que exibe uma saudacao com os parametros saudacao e nome
"""


# def msg(saudacao, nome):
#     return print(f'{saudacao}, {nome}!')
#
#
# nome = input('Digite seu nome: ')
# saudacao = input('Digite a saudacao desejada: ')
# msg(saudacao, nome)

"""
2 - Crie uma funcao que receba 3 numeros como parametros e exiba a soma entre eles
"""


# def adicao(n1, n2, n3):
#
#     if n1.isdigit() and n2.isdigit() and n3.isdigit():
#         n1 = int(n1)
#         n2 = int(n2)
#         n3 = int(n3)
#         return n1 + n2 + n3
#     else:
#         return
#
#
# n1 = input('Digite o primeiro numero: ')
# n2 = input('Digite o segundo numero: ')
# n3 = input('Digite o terceiro numero: ')
# soma = adicao((n1), (n2), (n3))
# if soma:
#     print(f'A somatoria dos numeros eh: {soma}')
# else:
#     print(f'Digite numeros validos')

"""
3 - Crie uma funcao que receba 2 numeros. O primeiro valor eh um valor e o segundo um percentual
(ex. 10%). Retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo.
"""


# def acrescimo(num, per):
#     if num.isdigit() and per.isdigit():
#         acresc = 0
#         num = int(num)
#         per = int(per)
#         per = per / 100
#         acresc = num * per
#         num += acresc
#         return num
#     else:
#         return
#
# n1 = input('Digite um numero: ')
# p1 = input('Digite a porcentagem do acrescimo: ')
#
# total = acrescimo(n1, p1)
# if total:
#     print(f'O valor final com acrescimo eh igual a: {total}')
# else:
#     print(f'Digite valores validos!')



"""
4 - Fizz Buzz - Se o parametro da funcao for divisivel por 2, retorne fizz,
se o parametro da funcao for divisivel por 5, retorne buzz. Se o parametro da funcao for
divisivel por 5 e 3, retorne FizzBuzz, caso contrario, retorne o numero enviado
"""


def fizzbuzz (n1):
    if n1.isdigit():
        n1 = int(n1)
        if n1 % 5 == 0 and n1 % 3 == 0:
            return 'FizzBuzz'
        if n1 % 5 == 0:
            return 'Buzz'
        if n1 % 3 == 0:
            return 'Fizz'
        return n1
    else:
        return


numero = input('Digite um numero: ')
val = fizzbuzz(numero)
if val:
    print(val)
else:
    print(f'Digite um valor valido!')
