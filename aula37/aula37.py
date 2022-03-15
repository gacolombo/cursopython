perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto eh 2+2',
        'respostas': {'a': '1', 'b': '4', 'c': '8'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto eh 5+5',
        'respostas': {'a': '10', 'b': '52', 'c': '15'},
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto eh 5x5',
        'respostas': {'a': '10', 'b': '25', 'c': '15'},
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto eh 10x10',
        'respostas': {'a': '110', 'b': '1000', 'c': '100'},
        'resposta_certa': 'c',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto eh 20+20',
        'respostas': {'a': '41', 'b': '200', 'c': '40'},
        'resposta_certa': 'c',
    }
}

print()
respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Escolha UMA entre as opcoes abaixo')
    for rk, rv in pv['respostas'].items():
        print(f'{rk}) {rv}')

    respostas_usuario = input('Sua resposta: ')
    if respostas_usuario == pv['resposta_certa']:
        print('Voce acertou! :D')
        respostas_certas += 1
    else:
        print('Voce errou... :(')
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acertou foi: {porcentagem_acerto}%')