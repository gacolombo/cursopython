"""
while em python - aula 19
utilizado para realizar acoes enquanto
uma condicao for verdadeira

Requisitos: Entender condicoes e operadores
"""
ver = True

while ver:
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operacao = input('Qual operacao deseja fazer? ')
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if operacao == '+':
            valor = num1 + num2
            print(f'{num1} + {num2} = {valor}')
        elif operacao == '-':
            valor = num1 - num2
            print(f'{num1} - {num2} = {valor}')
        elif operacao == '*':
            valor = num1 * num2
            print(f'{num1} * {num2} = {valor}')
        elif operacao == '/':
            valor = num1 / num2
            print(f'{num1} / {num2} = {valor}')
        else:
            print('Digite uma operacao valida')
            continue
    else:
        print('Digite um numero inteiro')
        continue

    resp = input('Deseja continuar?(S/N) ')
    resp = resp.upper()
    if resp == 'S':
        continue
    else:
        break
