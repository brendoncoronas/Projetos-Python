"""
cria uma função que multiplica todos os argumentos
não nomeados recebidos
retorne o total para uma variavel e mostre o valor
da variavel.
"""

def multiplicar(*args): 
    total = 1 
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(1, 2, 3, 4, 5) 
print(multiplicacao)

