# faça um projeto que calcule
# o numero passado pelo


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
    
    
