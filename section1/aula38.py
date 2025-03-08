'''
Desempacotando em chamadas
de métodos e funções
'''

string = 'ABCD'
lista = ['Maria', 'Helena', 1 , 2, 3, 'Eduarda']
tupla = 'python,', 'é', 'legal'

salas = [
    # 0           1
    ['Maria', 'Helena', ],  # 0 -> Lista zero

    # 0
    ['Elaine', ], # 1 -> Lista um

    # 0        1        2
    ['Luiz', 'João', 'Eduardo', ] # 2 -> Lista dois
]

# a, b, *_, ap, c = lista
# print(a, c, ap)

# for nome in lista:
#     print(nome, end=' ')

# print('Maria Helena 1 2 3 Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')
