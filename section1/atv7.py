''' Calculadora com while '''

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite um outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos números, ou ambos, são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas 1 operador.')
        continue

    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'A soma dos números {num_1_float} e {num_2_float} é igual a {soma}')
        print()
        
    elif operador == '-':
        subtração = num_1_float - num_2_float
        print(f'A subtração dos números {num_1_float} e {num_2_float} é igual a {subtração}')
        print()
        
    elif operador == '*':
        multiplicação = num_1_float * num_2_float
        print(f'A multiplicação dos números {num_1_float} e {num_2_float} é igual a {multiplicação}')
        print()
        
    elif operador == '/':
        divisão = num_1_float / num_2_float
        print(f'A divisão dos números {num_1_float} e {num_2_float} é igual a {divisão}')
        print()
    else:
        print('Nunca deveria chegar aqui!')    


    sair = input('Quer sair [s]im ou [n]ão: ').lower().startswith('s')
    

    if sair is True:
        break
    else:
        continue
