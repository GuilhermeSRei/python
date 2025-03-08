'''
Argumentos nomeados e não nomeados em função python
Argumentos nomeados tem com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''

def soma(x, y):
    # Definição
    print(f'{x=} e {y=}, x + y = {x + y}')

# Argumento posicional:
soma(10, 20)

# Argumentos nomeados:
soma(y=2, x=1)