# faça um projeto que temos que
# adivinhar uma determinada palavra
#


import os

palavra_secreta = 'perfume'
letra_acertadas = ''
numeros_tentativas = 0 


while True:
    letra_digitada = input('digite uma letra:')
    numeros_tentativas += 1

    if len(letra_digitada) > 1:
        print('figite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letra_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

    print('palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')

        print('VOCÊ GANHOU!! PARABÊNS!')
        print('a palavra era', palavra_secreta)     
        print('Tentativas:', numeros_tentativas)   
        
        letra_acertadas = ''
        numeros_tentativas = 0










