"""
ideia de projeto:

crie uma funçao que encontra o primeiro duplicado considerando o segundo
número como a duplicação. retorne a duplicação considerada.
requisitos:
    a ordem do numero duplicado é considerado a partir da segunda
    ocorrencia do numero, ou seja, o numero duplicado em si.
    exemplo:
    [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3, pois é o primeiro duplicado considerando a ordem de seu par)
    [1, 2, 3, 4, 5, 6] -> retorne -1 (não tem duplicados)
se não ocorrer duplicados na lista, retorne -1    
"""

lista_de_lista_de_inteiros = 
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1,],
]

def encontra_primeiro_duplicado(lista_de_inteiros
    numeros_checados = set()
    primeiro_duplicado = -1  # como padrão ja iniciaremos com o -1

    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero # isso ira ser verdadeiro caso um numero apareça pela segunda vez
            break 

        numeros_checados.add(numero

    return primeiro_duplicado

for lista in lista_de_lista_de_inteiros:  # nosso def esta agr recebendo as nossas listas 
   print(
    
    lista, 
    encontra_primeiro_duplicado(lista)  
    

