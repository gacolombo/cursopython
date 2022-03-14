"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
"Seu nome é curto"; se tiver entre 5 e 6 letras, escreva: "Seu nome é médio"; maior que 6 letras
escreva: "Seu nome é muito grande".
"""

# num1 = input('Digite um numero: ')
#
# if num1.isdigit():
#     num1 = int(num1)
#     ver_par = num1 % 2
#     if ver_par == 0:
#         print('O numero informado e PAR')
#     else:
#         print('O numero informado e IMPAR')
# else:
#     print('ERROR! Digite um numero inteiro')

# horario = input('Digite as horas: ')
# if horario.isdigit():
#     horario = int(horario)
#     if horario <= 11:
#         print('Bom dia!')
#     elif horario <= 17:
#         print('Boa tarde!')
#     else:
#         print('Boa noite!')
# else:
#     print('Digite um horario valido')

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print('Seu nome e curto')
elif tamanho_nome <= 6:
    print('Seu nome e medio')
else:
    print('Seu nome e grande')
