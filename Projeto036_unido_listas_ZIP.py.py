

# crie uma função zipper 
# o trabalho dessa função será unir duas 
# listas na oreem.
# use todos os valores da menor lista.

from itertools import zip_longest


l1 = ['salvador', 'ubatuba', 'belo horizonte'
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip_longest(l1, l2, fillvalue='sem cidade(rj)'