
# Questão 1

# numero = input('Digite um número: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     if (numero_int % 2) == 0:
#         print(f'O número {numero_int} é par')
#     else:
#         print(f'O número {numero_int} é ímpar')
# else:
#     print('Você não digitou um número inteiro')

#                    OU

# numero = input('Digite um número: ')

# try:
#     numero_int = int(numero)
#     if (numero_int % 2) == 0:
#         print(f'O número {numero_int} é par')
#     else:
#         print(f'O número {numero_int} é ímpar')
# except:
#     print('Você não digitou um número inteiro')

# Questão 2

# hora = int(input('Que horas são? '))

# if hora >= 0 and hora < 12:
#     print('Bom dia!')
# elif hora >= 12 and hora < 18:
#     print('Boa tarde!')
# elif hora >= 18 and hora <= 23:
#     print('Boa noite!')

# # Questão 3

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
if nome:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    elif tamanho_nome > 6:
        print('Seu nome é grande')
else:
    print('Digite algo')