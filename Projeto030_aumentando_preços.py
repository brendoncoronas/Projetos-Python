
import copy

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]


# aumentar os preços dos produtos a seguir em 10%
# gerar novo_produtos por deep copy (copia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos
]
