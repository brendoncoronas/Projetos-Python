"""
CPF: 746.824.890-70
colete a soma dos 9 primeiros numeros digitados do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

ex.: 746.824.890-70 (746824890)
   10  9   8   7   6  5   4   3   2
   7   4   6   8   2  4   8   9   0
   70  36  48  56  12 20  32  27  0

somar todos os resultados:
70+ 36+48+56+12+20+32+27+0 = 301
multiplicar o resultado anterior por 10

301 * 10 = 3010
obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
se o resultado anterior for maior que 9:
    resultado é 0
contrario disso:
    resultado é o valor da conta
"""

import re
import sys

entrada = input('CPF:')

cpf_enviado_usuario = re.sub(
    r'[^0-9]', # qremos substituir qualquer coisa q n seja um numero de 0 a 9 (por isso usamos o ^)
    '', # e tudo q n for um numero substitua para o q esta entre aspas, q no caso é nada.
    entrada
    )  

entrada_e_sequencial = entrada == entrada[0] * len(entrada)
if entrada_e_sequencial:
    print('voce enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10
resultado_1 = 0 
for digito in nove_digitos  :
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1  # cada volta do laço diminui 1

digito_1 = (resultado_1 * 10) % 11

digito_1 = digito_1 if digito_1 <= 9 else 0  

# vamos calcular o segundo digito
# devemos incluir o digito que acabamos de calcular

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é valido.')

else:
    print('CPF é invalido.')

      
