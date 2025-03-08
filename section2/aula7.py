'''
Higher Oder Functions
Funções de primeira classe
'''

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Guilherme')
)

print(
    executa(saudacao, 'Bom dia', 'Maria')
)
