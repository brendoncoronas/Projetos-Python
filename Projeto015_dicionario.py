# faça um projeto que faça uso de dicionarios
# que mostre bastante uso 

perguntas = 
    'pergunta1': {
        'pergunta': 'quanto é 1+1??',
        'respostas':{'a':'1','b':'2','c':'3'},
        'resposta_certa': 'b',},
    'pergunta2': {
        'pergunta': 'quanto é 3-1??',
        'respostas':{'a':'2','b':'4','c':'3'},
        'resposta_certa': 'a'},
    'pergunta3': {
        'pergunta': 'quanto é 5-5??',
        'respostas':{'a':'1','b':'2','c':'0'},
        'resposta_certa': 'c'},
}
print('jogo de perguntas e respostas:')
print()
respostas_certas = 0

for pk,pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('respostas:')

    for rk,rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usurio = input('sua resposta:')


    if resposta_usurio == pv['resposta_certa']:
        print('UHUUUULL!! VOCE ACERTOU!!!')
        respostas_certas += 1
    else:
        print('NAO FOI DESSA VEZ...')

qtd_perguntas = len(perguntas)
porcentagem_acertos = respostas_certas / qtd_perguntas * 100
print(f'voce acertou {respostas_certas} perguntas.')
print(f'sua porcentagem de acerto foi de {porcentagem_acertos:.2f}%.')
