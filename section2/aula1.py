'''
Introdução às funções (def) em python
Função são trechos de código usados para
replicar determinadas ação ao longo do seu código.
Elas podem recerber valores para parametros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
'''

def multiplo_de (numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo}', end = ' ')
    print (resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

