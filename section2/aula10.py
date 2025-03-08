'''
Manipulando chaves e valores em dicionários
'''

# pessoa = {
#     'nome': 'Guilherme',
#     'Sobrenome': 'Reis',
#     'idade': 21,
#     'altura': 1.74,
#     'endereço': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outra rua', 'numero': 456},
#     ]
# }

pessoa = {}

# Criando chaves
chave = 'nome'
pessoa[chave] = 'Guilherme'
pessoa['sobrenome'] = 'Reis'

print(pessoa)

# Alterando valor
pessoa[chave] = 'Gabriel'

print(pessoa[chave])

# Deletando chave
del pessoa['sobrenome']
print(pessoa)

