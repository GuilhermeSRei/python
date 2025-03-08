#                                 Operadores IN e NOT IN

#  Strings são interáveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('á' in nome) # True
# print('z' in nome) # False
# print('vio' in nome)

# print(10 * '-')

# print('vio' not in nome) # False
# print('zero' not in nome) # True

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está dentro de {nome}')
else:
    print(f'{encontrar} não está em {nome}')