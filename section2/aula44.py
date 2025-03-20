# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'fabrício', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Guilherme', 'nota': 'B'},
    {'nome': 'Lucas', 'nota': 'B'},
    {'nome': 'João Paulo', 'nota': 'C'},
    {'nome': 'Juliane', 'nota': 'D'},
    {'nome': 'camile', 'nota': 'B'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)