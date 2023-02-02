"""
Faça um programa que pergunte a hora ao usuario e, baseando se no horario
descrito, exiba a saudação apropriada. EX.
bom dia 0-11, boa tarde 12-17 ,boa noite 18-23 
"""

entrada = input('digite a hora em numeros inteiros:')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('bom dia.')
    
    elif hora >= 12 and hora <= 17:
        print('boa tarde.')

    elif hora >= 18 and hora <= 23:
        print('boa noite.')
        
    else:
        print('nao conheço essa hora.')
        
except:
    print('por favor, digite apenas numeros inteiros.')
