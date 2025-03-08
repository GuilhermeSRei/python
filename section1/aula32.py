'''
Introdução ao desempacotamento + tuples (tuplas)
'''
#Qualquer interável pode ser feito isso
# nomes = ['Maria', 'Helena', 'José']
# nome1, nome2, nome3 = nomes
# nome1, nome2, nome3 = ['Maria', 'Helena', 'José']
# print(nome2) => 'Helena'

# Erro
# nome1, nome2 = ['Maria', 'Helena', 'José']
# print(nome2)

# Erro
# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'José']

# Usa o *_ para indicar que não será mais usada essa variavel
# nome1, *_ = ['Maria', 'Helena', 'José']
# print(nome1)
# print(_)

_, _, nome, *_ = ['Maria', 'Helena', 'José']
print(nome)
print(_)
