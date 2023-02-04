"""
iterando strings com while
"""

# nome = 'luiz otavio'
# novo_nome = ''
# indice = 0
# while indice < len(nome):  # enqunto o indice for menor que o tamanho da string
#     letra = nome[indice]   # pega o nome e pega o indice atual em q o while esta a cada laço pega uma letra (qremos q letra pegue os mesmo indices q a variavel 'indice') (FAZ COM Q A VAR 'LETRA' RECEBA O VALOR DOS INDICES EM Q O LAÇO SE ENCONTRA)
#     novo_nome += f'*{letra}'  # a cada letra q for add sera add tbm um *
#     indice += 1

# print(novo_nome)

###############


nome = 'brendon'
novo_nome = ''
i = 0

while i < len(nome):
    letra = nome[i]
    novo_nome += f'*{letra}'

    i += 1

print(novo_nome)    



