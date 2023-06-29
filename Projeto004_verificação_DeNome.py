# irei adicionar um mini texto introdutório

"""
fazer um programa qur peça o primeiro nome do usuario. se o nome tiver 4 letras ou menos
escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva "seu nome é normal";
maior que 6 escreva "seu nome é muito grande"
"""

nome = input('digite seu nome:')

tamanho_nome = len(nome)

if tamanho_nome>= 1:
    if tamanho_nome <= 4:
        print('seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <=6
        print('seu nome é normal.')
    else:
        print('seu nome é muito grande.')        

else:
    print('digite mais de uma letra')

