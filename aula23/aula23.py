"""
listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce PERDEU!!')
        break
    else:
        letra = input('Digita uma letra: ')

        if len(letra) > 1:
            print('Digite apenas UMA letra!')
            continue
        digitadas.append(letra)

        if letra in secreto:
            print(f'Eba, a letra "{letra}" existe na palavra secreta.')
            print(f'Voce ainda tem {chances} chances!')
        else:
            print(f'Poxa, a letra "{letra}" NAO EXISTE na palavra secreta... :(')
            digitadas.pop()
            chances -= 1
            print(f'Voce ainda tem {chances} chances!')
        secreto_temporario = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'
        if secreto_temporario == secreto:
            print('Que legal voce ganhou...')
            print(secreto_temporario)
            break
        else:
            print(f'A palavra secreta esta assim: {secreto_temporario}')