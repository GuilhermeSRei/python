
#                               Operadores Aritméticos

adicao = 10 + 10
print('Adição', adicao)

subtração = 10 - 5
print('Subtração', subtração)

multiplicação = 10 * 10
print('Multiplicação', multiplicação)

divisao = 10 / 2.2 # float
print('Divisão', divisao)

divisao_inteira = 10 // 2.2 # float, ela da um valor mais próximo do inteiro
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2 # resto da divisão
print('Modulo', modulo)

print(10 % 8 == 0) # 10 é divisivel por 8? Não
print(16 % 8 == 0) # 16 é divisilvel po 8? Sim
print(10 % 2 == 0) # 10 é par? Sim
print(13 % 2 == 0) # 15 é par? Não

print()

# ---------------------------------------------------------------------------------------------

#                          Concatenação e repetição com operadores

concatenacao = 'A' + 'B' + 'C'
print(concatenacao)


a_dez_vezes = 'A + ' * 10
tres_vezes_luz = 3 * 'Luz '
print(a_dez_vezes)
print(tres_vezes_luz)
print()
# ----------------------------------------------------------------------------------------------

#                                   Precedência dos Operaores

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)

