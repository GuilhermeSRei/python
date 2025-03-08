'''
Lista em Python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - índice e fatiamento
Métodos uteis: append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete
Criar, Ler, Alterar, Apagar = lista[i](CRUD)
'''
#         01234
#        -54321
# string = 'ABCDE' # 5 caracteres

# # print(bool(lista)) ==> falsy
# # print(lista, type(lista))

# #         0     1        2        3    4
# #        -5    -4       -3       -2   -1
# lista = [123, True, 'Guilherme', 1.2, []]
# lista[-3] = 'Maria'
# print(lista)
# print(lista[2], type(lista[2]))


# ----------------------------------------------------------------------------------------------------

lista = [10, 20, 30, 40]
# lista[2] = 300
# print(lista)
# print(lista[2])

# print()

# del lista[2]
# print(lista)
# print(lista[2])

lista.append(50)
lista.pop() # Remove o ultimo elemento da lista (50)
lista.append(60)
lista.append(70)
# ultimo_valor = lista.pop() # Remove o ultimo elemento da lista (70)
valor_removido = lista.pop(3)
print(lista, 'Removido', valor_removido)
