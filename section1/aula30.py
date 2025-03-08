'''
Cuidados com dados mutaveis
= - copiando o valor (imutavel)
= - apontando para o mesmo valor na memoria (mutável)
'''

# Um apelido pode apontar para valores diferente,
# Como o APELIDO NOME está apontando em primeiro momento no VALOR GUILHERME
# e depois é direcionado para o VALOR JOÃO

# Apelido = Valor

# nome = 'Guilherme'
# print(nome)
# nome = 'João'
# print(nome)

#-----------------------------------------------------------
# Dois ou mais apelido de lista podem apontar oara um mesmo valor,
# Como o APELIDO LISTA_A está apontando para o VALOR LISTA GUILHERME E JOSÉ
# e o APELIDO LISTA_B também está apontado para o VALOR DA LISTA_A, GUILHERME E JOSÉ

# Apelido = Valor (list)

lista_a = ['Guilherme', 'José', 1, True, 1.2]
lista_b = lista_a

print(lista_a)
print(lista_b)

lista_a[0] = 'Qualquer coisa' # Modificou a lista_a, mas a variavel lista_b tbm foi alterada
print(lista_b)

#---------------------------------------------------------------------

lista_a = ['Guilherme', 'José', 1, True, 1.2]
lista_b = lista_a.copy() # Copia a lista para outra lista

print(lista_b)

