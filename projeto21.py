"""
faça um programa que peça ao usuario para digitar um numero inteira,
informe se este numero é par ou impar. caso o usuario nao digite um numero
inteiro, infome que nao é um numero
"""

entrada = input('digite um numero:')
try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:  #se par_impar retornar True executara o codigo
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}.') 

except:
    print('voce não digitou um numero inteiro.')