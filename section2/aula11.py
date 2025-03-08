'''
Métodos uteis dos dicionários em python
'''

pessoa = {
    'nome': 'Guilherme',
    'Sobrenome': 'Reis',
}

# len
# print(len(pessoa))

# keys
# print(tuple(pessoa.keys()))

# values
# print(list(pessoa.values()))

# items
# print(list(pessoa.items()))

# setdefault
# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])
'''
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

'''
# copy
# d2 = d1.copy()
# d2['l1'][1] = 999

# d2['c1'] = 1000
# print(d1)
# print(d2)

# get
# print(pessoa.get('nome'))

# pop
# print(pessoa)
# nome = pessoa.pop('nome')
# print(nome)
# print(pessoa)

# popitem
# print(pessoa)
# ultima_chave = pessoa.popitem()
# print(ultima_chave)
# print(pessoa)

# update

pessoa.update({
    'nome': 'Novo valor',
    'idade': 30,
})

print(pessoa)