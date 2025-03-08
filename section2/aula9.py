'''
Dicionários em python (tipo dict)
'''
# Imutáveis: str, int, float, bool, tuple
# Mutavel: dict, list

pessoa = {
    'nome': 'Guilherme',
    'Sobrenome': 'Reis',
    'idade': 21,
    'altura': 1.74,
    'endereço': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 456},
    ]
}

#print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['idade'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])