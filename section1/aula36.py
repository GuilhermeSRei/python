'''
Split e join com list e str
split - divide uma string (list)
join - une uma string
'''
frase = '     Olha só que  , coisa interessante    '
lista_de_frases_crua = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_de_frases_crua):
    lista_frases.append(lista_de_frases_crua[i].strip()) 
    # rstrip- Direta, lstrip - Esquerda

# print(lista_de_frases_crua)
# print(lista_frases)

frases_unidas = ', '.join(lista_frases) # join(interaveis)
print(frases_unidas)
