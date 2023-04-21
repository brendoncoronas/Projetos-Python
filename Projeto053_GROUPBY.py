from  itertools import groupby

alunos = [
    {'nome': 'luiz', 'nota': 'A'}
    {'nome': 'leticia', 'nota': 'B'
    {'nome': 'fabricio', 'nota': 'A'
    {'nome': 'rosemary', 'nota': 'C'
    {'nome': 'joana', 'nota': 'D'
    {'nome': 'joao', 'nota': 'A'
]


def ordena(aluno:   # estamos ordenando por nota
    return aluno['nota'

alunos_agrupados = sorted(alunos, key=ordena

grupos = groupby(alunos_agrupados, key=ordena

for chave, grupo in grupos:
    print(chave
    for aluno in grupos:
        print(aluno
