# faça um projeto que mostre o uso de polimorfismo


from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod   
    def fala(self, msg): pass

class B(A):
    def falar(self, msg):
        print(f'B esta falando {msg}')


class C(A):
    def falar(self, msg):
        print(f'C esta falando {msg}')



b = B()
c = C()
b.fala('um assunto')
c.fala('outro assunto')
