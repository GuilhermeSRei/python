# Introdução à List Comprehension em python
# List comprehension é uma forma rápisa para criar listas
# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# # print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
#     ]
# print(list(range(10)))
# print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
]

novos_produtos = [
    # {'nome': produto['nome'], 'preço': produto['preço']}
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto} # if de condicionamento
    for produto in produtos
]

print(type(novos_produtos))
print(*novos_produtos, sep='\n')