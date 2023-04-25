# faça um 

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('metaclass new')
        cls = super().__new__(mcs, name, bases, dct)
        cls.attr = 1234
        return cls


class Pessoa(metaclass=Meta):
    def __new__(cls, *args, **kwargs) 
        print('meu new')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('meu init')
        self.nome = nome

p1 = Pessoa('luiz') 
print(p1.attr)
