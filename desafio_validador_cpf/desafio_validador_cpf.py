"""
CPF = 168.955.350-09
------------------------------------------
1 * 10 = 10                     #   1 * 11 = 11
6 * 9 = 54                      #   6 * 10 = 60
8 * 8 = 64                      #   8 * 9 = 72
9 * 7 = 63                      #   9 * 8 = 72
9 * 6 = 54                      #   9 * 7 = 63
5 * 5 = 25                      #   5 * 6 = 30
3 * 4 = 12                      #   3 * 5 = 15
5 * 3 = 15                      #   5 * 4 = 20
0 * 2 = 0                       #   0 * 3 = 0
                                #-> 0 * 2 = 0
        297                     #           343
11 - (297 % 11) = 11            #   11 - (343 % 11) = 9
11 > 9 = 0                      #
Digito 1 = 0                    #   Digito 2 = 9
"""
from random import randint
cpf = str(randint(100000000, 999999999))
p = 12
digito1 = 0
digito2 = 0
soma1 = 0
soma2 = 0
calc1 = 0
calc2 = 0

novo_cpf = cpf
for a, r in enumerate(range(10, 1, -1)):
    p = p - 1
    num = novo_cpf[a]
    calc1 = int(num) * r
    calc2 = int(num) * p
    soma1 = soma1 + calc1
    soma2 = soma2 + calc2
    # print(f'{num} * {r} = {calc1} {soma1} | {num} * {p} = {calc2} {soma2}')
digito1 = 11 - (soma1 % 11)
if digito1 > 9:
    digito1 = 0
# print(digito1)
soma2 = soma2 + (digito1 * 2)
# print(soma2)
digito2 = 11 - (soma2 % 11)
# print(digito2)
novo_cpf = novo_cpf + str(digito1) + str(digito2)
print(novo_cpf)