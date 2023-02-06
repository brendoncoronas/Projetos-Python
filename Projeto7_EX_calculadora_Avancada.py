""" calculadora com while """

while True:
    num_1 =  input('digite um numero:')
    num_2 =  input('digite outro numero:')
    operador =  input('digite o operador (-+/*):')
    
    numeros_validos = None

    num_1_float = 0 # estamos definindo as 2 variaveis fora do laço,boa pratica de conduta
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True  # estamos usando essa VAR para checagem, se n gerar erro no try logo ela se torna True

    except:    
        numeros_validos = None

    if numeros_validos is None:
        print('um ou ambos os numeros digitados são invalidos.') 
        continue   

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador invalidos.') 
        continue 

    if len(operador) > 1:  # se digitar mais q um operador
        print('digite apenas um operador.') 
        continue 
    
    print('realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)

    if operador == '-':
        print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)

    if operador == '/':
        print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)

    if operador == '*':
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)


    sair = input('deseja sair? [s]im:').lower().startswith('s') 

    if sair is True:
        print('voce saiu da calculadora.')
        break
