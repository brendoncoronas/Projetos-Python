impo

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('voce nao passou argumentos')
else:
    try:
        print(f'voce passou o argumento {argumentos[0]}')

    except IndexError:
        print('faltam argumentos')

