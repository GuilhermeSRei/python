"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
def zipper(lista_a, lista_b):
    intervalo = min(len(lista_a), len(lista_b))
    return [ lista_a[i] + lista_b[i] for i in range(intervalo) ]
    

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

print(zipper(lista_a, lista_b))
#-------------------------------------------------------------

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(f'\n{lista_soma}')