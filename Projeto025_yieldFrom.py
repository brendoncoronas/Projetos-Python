# faça uma função que mostre

def gen1():
    print('começou GEN1')
    yield 1
    yield 2
    yield 3
    print('acabou GEN1')

def gen3():
    print('começou GEN3')
    yield 10
    yield 20
    yield 30
    print('terminou GEN3')


def gen2(gen):
    print('começou GEN2')
    yield from gen()  
    yield 4
    yield 5
    yield 6
    print('acabou GEN2')


g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)

for numero in g2:
    print(numero)
