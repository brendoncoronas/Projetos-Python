
# um bom codigo é aquele que nao fica se repetindo
# superClasse   a herança funciona de cima para baixo
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__  

    def falar(self):  
        print(f'{self.nomeClasse} Falando...'


# SubClasse
class Cliente(
    Pessoa):  
    def comprar(self):  
        print(f'{self.nomeClasse} comprando...'

    def falar(self):
        print(f'voce esta em CLIENTE.'


# SubClasse
class Aluno(Pessoa):  
    def estudar(self): 
        print(f'{self.nomeClasse} esta estudando...'


class ClienteVIP(Cliente):  
    def falar(self):  
        super().falar()  
        Pessoa.falar(self)  
        Cliente.falar(self)
        print('qualquer outra coisa.')
        print(f'{self.nome} {self.sobrenome}'

    def __init__(self, nome, idade, sobrenome):  
        super().__init__(nome, idade)  
        self.sobrenome = sobrenome