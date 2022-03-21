#add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estao nos dois sets, mas nao em ambos)

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1.intersection(s1, s2)

print(s3)