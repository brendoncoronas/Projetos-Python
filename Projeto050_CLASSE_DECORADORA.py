# classes decoradora
# faça um projeto que mostre o uso
# claro de uma classe decoradora

class Multiplicador:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
    
    def __call__(self, func): 
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        
        return interna

@Multiplicador(10)  
def soma(x, y):
    return x + y   

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
