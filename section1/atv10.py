
# lista = ['Maria', 'Helena', 'Luiz', 'José']
# indice = 0

# for nome in lista:

#     print(indice, nome)
#     indice += 1
#------------------------------------------------------------------------------------

lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista)) 

'''
O range estabelece um intervalo numérico como (0, 3),
sendo esse intervalor composto por: 0, 1, 2
O ultimo numero do intervalo numerico não é contado, e demostra a quantidade de valores
'''

for indice in indices:
    print(indice, lista[indice])
