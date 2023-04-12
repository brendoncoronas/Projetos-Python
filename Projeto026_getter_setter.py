# faça um projeto que mostre o ver
# uso de getter e setter

class Pessoa:
    def __init__(self,nome):
        self._nome = nome

    @property  # getter ta retornando o valor
    def nome(self):
        return self._nome

    @nome.setter  
    def nome(self, nome): 
        self.atributo = nome  

p1 = Pessoa()
p1.nome = 'joao'
print(p1.nome)
