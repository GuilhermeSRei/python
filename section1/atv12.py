'''
Gerando o primeiro digito de um CPF
'''

# cpf = [7, 4, 6, 8, 2, 4, 8, 9, 0]
# num = 10
# soma = 0




# # Multiplicação
# for indice, valor in enumerate(cpf):
#     digito = cpf[indice]
#     indice += 1

    
#     soma += digito * num
#     num -= 1

    


# operacao = (soma * 10) % 11
# # print(operacao)

# print('O primeiro digito do cpf é:')
# print(operacao if operacao <= 9 else 0)

#---------------------------------------------------------------------------------------------------

cpf = '74682489070'
nove_digito = cpf[0:9]

contador_regressivo_1 = 10

resultado_1 = 0

for digito in nove_digito:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_cpf_1 = (resultado_1 * 10) % 11
digito_cpf_1 = digito_cpf_1 if digito_cpf_1 <= 9 else 0

print(f'O primeiro digito do cpf é: {digito_cpf_1}')

    
