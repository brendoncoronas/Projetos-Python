# faça um projeto que mostre o uso
# claro de clo

def  criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar     # importante retornar a funcao sem executar

falar_bom_dia = criar_saudacao('bom dia')
falar_boa_noite = criar_saudacao('boa noite')

for nome in ['maria', 'joão', 'laura']:
    print(falar_boa_noite(nome))
    print(falar_bom_dia(nome))
