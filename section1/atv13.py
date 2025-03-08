# Primeiro Digito
cpf_enviado = '74682489070'
nove_digito = cpf_enviado[:9]

contador_regressivo_1 = 10

resultado_1 = 0
for digito in nove_digito:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_cpf_1 = (resultado_1 * 10) % 11
digito_cpf_1 = digito_cpf_1 if digito_cpf_1 <= 9 else 0
digito_1 = str(digito_cpf_1)
print(f'O primeiro digito é {digito_1}')

# Segundo Digito
dez_digito = nove_digito + digito_1

contador_regressivo_2 = 11

resultado_2 = 0
for digito in dez_digito:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_cpf_2 = (resultado_2 * 10) % 11
digito_cpf_2 = 0 if digito_cpf_2 > 9 else digito_cpf_2
digito_2 = str(digito_cpf_2)
print(f'O segundo digito é {digito_2}')

cpf_gerado = f'{nove_digito}{digito_1}{digito_2}'

# Validando cpf de maneira simples

if cpf_enviado == cpf_gerado:
    print(f'{cpf_enviado} é válido')
else:
    print(f'CPF não é válido')

