# faça um projeto que uma configura
from dataclasses import asdict, astuple, dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ = __main__:
    p1 = Pessoa('luiz', 'otavio')
    print(asdict(p1)  # podemos manipular normalmente como um dicionario ou
    print(astuple(p1)  # uma tupla
