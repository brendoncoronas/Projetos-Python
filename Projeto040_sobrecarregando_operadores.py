"""
no python, o comportamneto dos operadores é definido por metodos especiais.
vamos alterar o comportamento de operadores com classes definidas pelo usuario.
"""


class Retangulo:
    def __init__(self, x, y:
        self.x = x
        self.y = y

    def __repr__(self:
        return f"<class 'Retangulo({self.x}, {self.y})'>"  


    def __add__(self, other:  # vamos ensinar o interpretador do python a fazer essa soma
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)


r1 = Retangulo(10, 20
r2 = Retangulo(10, 20
r3 = r1 + r2
print(r3)