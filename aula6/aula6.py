"""
Iniciar com letra, pode conter numeros, separa _, letras minusculas
"""

nome = 'Gabriel'
idade = 24
altura = 1.81
maiorDeIdade = idade >= 18
peso = 92
imc = peso / altura ** 2

print(nome, type(nome))
print(idade, type(idade))
print(altura, type(altura))
print(maiorDeIdade, type(maiorDeIdade))
print(nome, 'tem', idade, 'anos de idade e tem o imc de:', imc)

