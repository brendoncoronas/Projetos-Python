# faça um projeto em que o codigo
# gere mais de cem CPFs
# dica: tera que importar um modulo


import random 

for _ in range(100):
    nove_digitos = ''

    for i in range(9):  
        nove_digitos += random.randint(0, 9)  

    contador_regressivo_1 = 10
    resultado_1 = 0 
    for digito in nove_digitos  :
        resultado_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1  # cada volta do laço diminui 1

    digito_1 = (resultado_1 * 10) % 11

    digito_1 = digito_1 if digito_1 <= 9 else 0  # digito vai ser igual a digito se digito for menor ou igual a 9, senão retorna 0
    
    # gerando segundo digito:

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
