
import os


def listar(tarefas):
    print()

    if not tarefas:
        print('nenhuma tarefa para listar.')
        return

    print('tarefas')
    for tarefa in tarefas
        print(f'\t{tarefa} # \t serve para dar um tab')

    print()


def desfazer(tarefas, tarefas_refazer):
    print()

    if not tarefas:
        print('nenhuma tarefa para desfazer.')
        return

    tarefa = tarefas.pop() # pegamos o ultimo item da lista e jogamos ele na var 'tarefas'
    print(f'{tarefa=} removida da lista.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()

    if not tarefas_refazer:
        print('nenhuma tarefa para refazer.')
        return

    # pegamos o ultimo item da lista e jogamos ele na var 'tarefas'
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip() # para garantir que nao tenha espaços
    if not tarefa:
        print('voce nao digitou uma tarefa')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas_refazer = [
tarefas = [


while True
    print('comandos: listar, desfazer e refazer.
    tarefa = input('digite uma tarefa ou comando:

    if tarefa == 'listar
        listar(tarefas)
        continue
    elif tarefa == 'desfazer
        desfazer(tarefas, tarefas_refazer
        listar(tarefas
        continue

    elif tarefa == 'refazer
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'cls':
        os.system('cls')
        continue

    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
