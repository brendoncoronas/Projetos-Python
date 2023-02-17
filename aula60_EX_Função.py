"""
crie uma função que multiplica todos os argumentos
não nomeados recebidos
retorne o total para uma variavel e mostre o valor
da variavel.
"""

def multiplicar(*args): 
    total = 1 # aqui como é multiplicação começamos do 1 pois qualquer numero vezes 0 é zero
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(1, 2, 3, 4, 5) # aqui passamos os numeros que vão ser enpacotados, para ai sim fazermos a conta no DEF
print(multiplicacao)


"""
criar uma função se o numero é par ou impar
retorne se o numero é par ou impar
"""



def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par.'

    
    return f'{numero} é impar.'     

print(par_impar(2))    
print(par_impar(3))    
print(par_impar(15))    
print(par_impar(16))    