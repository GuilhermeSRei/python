prinmeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite outro valor: ')

if prinmeiro_valor > segundo_valor:
    print(f'O primeiro valor {prinmeiro_valor} é maior que o segundo valor {segundo_valor}')
elif segundo_valor > prinmeiro_valor:
    print(f'O segundo valor {segundo_valor} é maior que o primeiro valor {prinmeiro_valor}')
elif prinmeiro_valor == segundo_valor:
    print(f'Os dois valores são iguais a {prinmeiro_valor}')
else:
    print('Erro, tente novamente')