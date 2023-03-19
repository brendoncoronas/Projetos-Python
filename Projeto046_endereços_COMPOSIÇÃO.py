# faça um projeto com 
# uso CLARO de composição
# de no minimo dois metodos 


class Cliente:
    def __init__(self, nome):
        self.nome = nome 
        self.endereco = []

    def inserir_endereco(self, rua, numero):
        self.endereco.append(Endereco(rua, numero)

    def listar_enderecos(self):
        for endereco in self.endereco:
            print(endereco.rua, endereco.numero)    

    def __del__(self):
        print('APAGANDO,', self.nome)   



class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero 

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)    

cliente1 = Cliente('maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('rua B', 6745)
