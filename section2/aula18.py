# Filto

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preço': 20, },
    {'nome': 'p2', 'preço': 10, },
    {'nome': 'p3', 'preço': 30, },
]

# print(type(novos_produtos))
# print(*novos_produtos, sep='\n')

novos_produtos = [
    # {'nome': produto['nome'], 'preço': produto['preço']}
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto} # if de condicionamento (if ternário)
    for produto in produtos
    if (produto['preço'] >= 20 and produto['preço'] * 1.05) > 10
]

p(novos_produtos)

#------------------------------------------------------------------------
# lista = [n for n in range(10) if n < 5] # if do filtro
# print(lista)
#-------------------------------------------------------------------------