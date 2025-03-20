# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


# def zipper(lista_a, lista_b):
#     intervalo_maximo = min(len(lista_a), len(lista_b))
#     return [
#         (lista_a[i], lista_b[i]) for i in range(intervalo_maximo)
#     ]

from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados)))