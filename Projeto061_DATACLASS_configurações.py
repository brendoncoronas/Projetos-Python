from dataclasses import asdict, astuple, dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ = __main__
    p1 = Pessoa('luiz', 'otavio')
    print(asdictp1)  # podemos manipular normalmente como um dicionario ou
    print(astuplep1)  # uma tupla
