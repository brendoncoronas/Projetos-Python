
# faça um projeto que mostre a
# usabilidade do 

salas = [
    # 0
    ['maria', 'helena',], # 0
    # 0
    ['elaina',], # 1
    #    0     1      2
    ['luiz', 'joao', 'eduardo',], # 2

]
print(salas[2][3][3])


for sala in salas: # para cada sala na variavel SALAS, retorne a sala
    print(f'a sala é {sala}')
    for aluno in sala:  #nota-se que sala é no singular # para cada aluna na SALA retorne o aluno
        print(aluno)
