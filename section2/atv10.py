
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

def ler(tarefas, caminho_arquivo):
      dados = []
      try:
           with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
                dados = json.load(arquivo)
      except FileNotFoundError:
          print('Arquivo não encontrado')
          salvar(tarefas, caminho_arquivo)
      return dados

def salvar(tarefas, caminho_arquivo):
     with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
           dados = json.dump(
                tarefas,
                arquivo,
                ensure_ascii=False,
                indent=2
                )
           return dados

CAMINHO_ARQUIVO = 'atv10.json'

tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

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
    salvar(tarefas, CAMINHO_ARQUIVO)

#     with open('atv10.json', 'w', encoding='utf8') as arquivo:
#      json.dump(
#           tarefas,
#           arquivo,
#           ensure_ascii=False,
#           indent=2
#      )


