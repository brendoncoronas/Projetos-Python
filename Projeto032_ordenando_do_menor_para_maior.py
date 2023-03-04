
# ordene os produtos por nome crecente (do menor para maior)
# gere produtos_ordenados_por_preco por deep copy (copia profunda)
import copy

produtos = [
    {'nome': 'produto 5', 'preco': 10.00},
    {'nome': 'produto 1', 'preco': 22.32},
    {'nome': 'produto 3', 'preco': 10.11},
    {'nome': 'produto 2', 'preco': 105.87},
    {'nome': 'produto 4', 'preco': 69.90},
]


produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
    
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n'
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n') 
