# lista = [10, 20, 30, 40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(12333)
# del lista[-1]
# # lista.clear()
# print(lista, nome)
#------------------------------------------------------------------
# lista = [10, 20, 30, 40]
# lista.insert(0, 5) # (indice, valor)
# print(lista)

#--------------------------------------------------------------------

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

print(lista_a)
print(lista_b)
print(lista_c)

lista_d = lista_a.extend(lista_b) # Mexe diretamente na lista indicada
print(lista_d, lista_a)


