'''
Valores padrão para parâmetros
Ao definir uma função, os parãmetros podem ter
valores padrão. caso o valor não seja enviado para o parãmetro, o valor padrão será usado.

Refatorar: editar o seu código.
'''


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}, {x + y + z}')
    else:
        print(f'{x=} {y=}, {x + y}')

soma(1, 2)
soma(3, 5)
soma(7, 9, 0)

# Caso queria saber se o usuario informou ou naõ um valor, utiliza-se o None para atribuir como valor inicial e não interferir no processo de resolução

# No caso acima, utilizou o None para saber se a pessoa atribuiu o valor 0 ou não na coordenada z, pois, caso atribui-se o valor zero no código antigo,
# esse valor não sero mostrado, pois se considera falsy, assim utilizou o critério de is not ou is None.