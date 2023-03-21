# crie um projeto com todas 
# que mostre todas as usabilidades
# do encapsulamento, na mesma classes


class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self:
        print(self.__private
        return 'metodo_publico'

    def _metodo_protegido(self:
        return '_metodo_protegido'
    
    def __metodo_private(self:
        return '__metodo_privado'
    
    
f = Foo()
print(f.metodo_publico)
print(f._metodo_protegido)
print(f.__metodo_private)
