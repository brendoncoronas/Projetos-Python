# enumerações na programação é usada em ocasioes onde temos
# um determinado numero de coisas. 
# Como visto nas aulas 

import enum  

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direcoes(enum.Enum:
    ESQUERDA = enum.auto() # enumera automaticamente
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()


print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)

# estamos imformando que direcao é do tipo de Direcoes


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('direção não encontrada')

    # {direcao.name} é so para aparecer o nome quando dermos print, sem isso aparece mais coisa alem do nome
    print(f'movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
