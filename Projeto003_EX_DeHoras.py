# faça um projeto que mostre a saudação adequad


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
