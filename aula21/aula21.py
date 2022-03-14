# Indices
# 0123456789.............................33

frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova_string = ''
maiscula = input('Que letra deseja colocar maiscula? ')

while contador < tamanho:
    letra = frase[contador]
    if letra == maiscula:
        nova_string += maiscula.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
