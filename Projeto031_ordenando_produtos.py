
# ordene os produtos por nome decrecente (do maior para menor)
# gere produtos_ordenados_por_nome por deep copy (copia profunda)

import copy

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},

]


produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse= True
)


print(*produtos_ordenados_por_nome, sep='\n'
print()

