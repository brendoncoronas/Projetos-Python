"""
faça uma lista de compras com listas
o usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
não permitir que o programa quebre com erros
de indices inexistentes na lista.
"""
import os

lista  = []

while True:
    print('selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar:')

    if opcao == 'i':
        os.system('cls')
        valor = input('valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice_str = input('escolha um indice para apagar:')

        try:
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print('por favor, digite numeros inteiros.')    

        except IndexError:
            print('indice não existe na lista.')   

        except Exception:
            print('erro desconhecido.')    

    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
   

    else:
        print('por favor, escolha i, a ou l.') 
        
        
