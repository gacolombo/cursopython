"""
Operadores Logicos - Aula 12
and, or, not
in e not in
"""
# nome = input('Digite o seu nome: ')
# nome = nome.lower()
#
# if 'a' in nome:
#     print('Existe a letra A no seu nome')
# else:
#     print('Nao tem A no seu nome')

usuario = input('Usuario: ')
senha = input('Senha: ')
usario_bd = 'gabriel'
senha_bd = 'dragao'

if usuario == usario_bd and senha == senha_bd:
    print('Logado com sucesso!')
else:
    print('Usuario ou senha invalidos.')