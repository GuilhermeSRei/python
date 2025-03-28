
import json
import os

def listar(tarefas):
        print()
        if not tarefas:
           print('Nenhuma tarefa para listar')
           return

        print('Tarefas: ')
        for tarefa in tarefas:
             print(f'\t{tarefa}')
        
        print()

def desfazer(tarefas, tarefas_refazer):
    print()

    if not tarefas:
         print('Nenhuma tarefa para desfazer')
         return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()

    if not tarefa:
         print('Você não tem nenhuma tarefa')
         return
         
    tarefas.append(tarefa)

    print()



def refazer(tarefas, tarefas_refazer):
    print()

    if not tarefas_refazer:
         print('Nenhuma tarefa para refazer')
         return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

    print()


tarefas = []
tarefas_refazer = []



# with open('atv10.json', 'r', encoding='utf8'):
#      json.load(
          
#      )

while True:

    print('Comandos: listar, desfazer, refazer, limpar')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
         'listar': lambda: listar(tarefas),
         'desfazer': lambda:  desfazer(tarefas, tarefas_refazer),
         'refazer': lambda: refazer(tarefas, tarefas_refazer),
         'limpar': lambda:  os.system('cls'),
         'adicionar': lambda:  adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa)if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()

    with open('atv10.json', 'w', encoding='utf8') as arquivo:
     json.dump(
          tarefas,
          arquivo,
          ensure_ascii=False,
          indent=2
     )


