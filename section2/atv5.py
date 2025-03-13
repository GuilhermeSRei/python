# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

def exibir(dicionario):
    for item in dicionario:
        print(f'{item}')

novos_produtos = copy.deepcopy(produtos)

for produto in novos_produtos:
    produto['preco'] = round(produto['preco'] * 1.1, 2)

produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)

produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda item: item['nome'], reverse=True)

produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)

produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key=lambda item: item['preco'])

print('Essa é a lista de produtos:')
exibir(produtos)
print()

print('Essa é a lista de novos produtos:')
exibir(novos_produtos)
print()

print('Essa é a lista de produtos ordenados por nome em ordem decrescente:')
exibir(produtos_ordenados_por_nome)
print()

print('Essa é a lista de produtos ordenados por preço em ordem crescente:')
exibir(produtos_ordenados_por_preco)

