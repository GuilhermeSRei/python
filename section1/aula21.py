
'''
Operadores de atribuição
= += -= *= /= //= **= %=
'''

contador = 0

while contador <= 100:
    contador += 1 # Essa é a parte mais importante do while, é o que mantém o laço no loop

    if contador == 6:
        print('Não vou mostrar o 6')
        continue # Pula o termo determinado

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')
