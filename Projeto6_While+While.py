qtd_linhas = 5
qtd_colunas = 5
# em caso de duvida usar o debug!!!
linha = 1

while linha <= qtd_linhas:
    coluna = 1
    print(linha)
    
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')  # para cada linha sao 5 voltas na coluna
        coluna += 1

    linha +=1

print('acabou.')    