
# iterando strings com while
# faça um projeto que itere sobre o
# nome, ou qualquer palavara, frase
# e modifique-a de alguma maneira


nome = 'brendon coronas'
novo_nome = ''
indice = 0
while indice < len(nome):  
    letra = nome[indice]  
    novo_nome += f'*{letra}'  
    indice += 1

print(novo_nome)
