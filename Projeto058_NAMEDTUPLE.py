# faça um projeto com o uso claro de NAMEDTUP

from typing import NamedTuple
from collections import namedtuple

Carta = namedtuple('carta', ['valor', 'naipe']) # type: ignore

as_espadas = Carta('A', 'espada')

print(as_espadas)
print(as_espadas.naipe)
print(as_espadas.valor)
