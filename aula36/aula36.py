
d1 = {
    1: 2,
    3: 4,
    5: 6,
}

d2 = {
    'a': 'b',
    'c': 'd',
}
d1.update(d2)
print(d1)

















# import copy
#
# d1 = { 1: 'a', 2: 'b', 3: 'c', 'd': ['Gabriel', 'Colombo']}
# v = copy.deepcopy(d1)
#
# v[1] = 'Luiz'
# v['d'][0] = 'Joaozinho'
#
# print(d1)
# print(v)





























# clientes = {
#     'clientes1': {
#         'nome': 'Gabriel',
#         'sobrenome': 'Colombo',
#     },
#     'clientes2': {
#         'nome': 'Naju',
#         'sobrenome': 'Rodrigues',
#     },
#     'clientes3': {
#         'nome': 'Paulo',
#         'sobrenome': 'Araujo',
#     },
#     'clientes4': {
#         'nome': 'Luciana',
#         'sobrenome': 'Fernandes',
#     },
#     'clientes5': {
#         'nome': 'Lorenzo',
#         'sobrenome': 'Januzzi',
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t{dados_k} = {dados_v}')






















# d1 = {
#     'chave1': 'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'Tupla',
# }
#
# print('chave1' in d1)
# print('valor' in d1.values())
#
# for k, v in d1.items():
#     print(k, v)


# print(d1)
# del d1['chave1']
# print(d1)


# d1['naoexiste'] = 'Passou a existir'
# d1.update({'nova_chave':'novo_valor'})
#
#
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))
#
#
# if 'naoexiste' in d1:
#     print(d1['naoexiste'])
#
#
# print('OI')

