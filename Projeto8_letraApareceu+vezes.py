
frase = 'o rato roeu a roupa do rei de roma, cole ne...'

qtd_apareceu_mais_vezes = 0 
letra_apareceu_mais_vezes = ''

i = 0 

while i < len(frase):
    letra_atual = frase[i]

    if i == ' ':
        i += 1 
        continue

    qtd_letra_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_letra_atual:
        qtd_apareceu_mais_vezes = qtd_letra_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1


print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" apareceu '
    f'{qtd_apareceu_mais_vezes}x')