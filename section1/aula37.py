'''
Lista de listas e sues indices
'''

salas = [
    # 0           1
    ['Maria', 'Helena', ],  # 0 -> Lista zero

    # 0
    ['Elaine', ], # 1 -> Lista um

    # 0        1        2
    ['Luiz', 'João', 'Eduardo', ] # 2 -> Lista dois
]

# print(salas[1][0]) # (lista maior[lista menor][indice da lista menor])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2]) # (lista maior [lista menor] [indice da lista menor] [indice do valor da lista dentro da menor])
# (salas [lista 2] [tupla] [indice da tupla])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
