# Faça um projeto de uso CLARO
# de AGREGAÇÃO com pelo menos 
# 2 metodos diferentes
#


class Carrinho
    def __init__(self)
        self._produtos = [

    def total(self)
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos): # jogamos todos os nossos produtos dentro dessa variavel com o asterisco
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)     
        print()

class Produto:
    def __init__(self, nome , preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('caneta', 1.25), Produto('camiseta', 20)
carrinho.inserir_produtos(p1, p2)
