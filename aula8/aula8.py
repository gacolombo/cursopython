"""
* Criar variaveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* criar variavel com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = "Gabriel"
idade = 24
altura = 1.81
peso = 92
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade, logo, nasceu em {ano_nascimento}, tem {altura} de altura e {peso}kgs, resultando num imc de {imc:.2f} este teste foi feito em {ano_atual}')