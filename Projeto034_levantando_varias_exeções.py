# try, except, else, finally

"""
levantar mais de uma exeção com raise, no mesmo codigo
"""
try:
    a = 8
    b = 0
    c = a / b # estamos silenciando uma erro, pois o try ira tentar executar e se mesmo assim nao conseguir
  
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('dividiu por zero')

except NameError:
    print('nome de alguma variavel não esta definido')

except (TypeError, IndexError) as error: 
    print('MSG:', error)


except Exception:
    print('erro desconhecido.')


