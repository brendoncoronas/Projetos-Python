
"""
fazer uma lista de tarefas com as seguintes opçoes:
    adicionar tarefa
    listar tarefa
    opçao de desfazer (a cada vez que chamarmos,desfaz a ultima ação)
    opção de refazer(a cada vez que chamarmos, refaz a ultima ação)
"""

def do_redo(todo_list,redo_list)
    if not redo_list:
        print('nada para refazer.')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)

def show_op(todo_list):
    print()
    print('tarefas:')
    print()
    print(todo_list)


def do_add(todo,todo_list):
    todo_list.append(todo)

def do_undo(todo_list,redo_list):
    if not todo_list:
        print('nada para desfazer.')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

if __name__== '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('digite uma tarefa undo,redo,ls:')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list,redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list,redo_list)
            continue

        do_add(todo,todo_list)

