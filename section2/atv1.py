

def multiplicacao(*args):
    total = 1

    for valores in args:
        # total = total *  valores
        total *= valores
    
    return total

teste_1 = multiplicacao(1, 2, 3, 4, 5)
print(teste_1)
# print()
# print(1 * 2 * 3 * 4 * 5)

#---------------------------------------------------------------------

def impar_par(n):

    # if n % 2 == 0:
    #     return print(f'O número {n} é par')
    # else:
    #     return print(f'O número {n} é ímpar')

    if n % 2 == 0:
        return print(f'O número {n} é par')
    return print(f'O número {n} é ímpar')

    

teste_2 = impar_par(2)
