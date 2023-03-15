
# faça um projeto no qual tenha uma classe pessoa
# que retorne nome dinamicamente e uma idade padrao.
# Na mesma classe crie um metodo no qual o padrao 
# seja um nome anonimo, porem a idade tem que ser dinamica

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey'    

    @classmethod
    def criar_com_50_anos(cls, nome:
        return cls(nome, 50) # cls esta retornando a propria classe Pessoa
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('anonima', idade)
    

p1 = Pessoa('joao', 34)
p2 = Pessoa.criar_com_50_anos('helena')
p3 = Pessoa.criar_sem_nome(23)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
