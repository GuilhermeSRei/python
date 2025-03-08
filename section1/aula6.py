
#                                         Input

# nome = input('Qual o seu nome? ')
# print(f'o seu é {nome}') #print(f'o seu é {nome=}') --> o seu nome=______ (como irá aparecer no terminal)

#--------------------------------------------------------------------------------------------------------------------
# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite o outro numero: ')
# print(f'a soma é {numero_1 + numero_2}') # Os números virá como str

# numero_1 = int(input('Digite um número: '))
# numero_2 = int(input('Digite o outro numero: '))
# print(f'A soma é {numero_1 + numero_2}') # converteu os número em int

#-----------------------------------------------------------------------------------------------------------------------

# Nesse código há uma 'filtragem' dos valores atribuidos as variaveis n1 e n2 pelas int_n1 e int_n2, assim o o código não irá quebrar antes dos usuários terminarem de colocar a informação

numero_1 = input('Digite um número: ') # Recebe os dados dos usuarios
numero_2 = input('Digite o outro numero: ')

int_numero_1 = int(numero_1) # transforma em inteiro
int_numero_2 = int(numero_2)

print(f'A soma é {int_numero_1 + int_numero_2}') # exibi a soma