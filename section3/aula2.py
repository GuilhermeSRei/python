# Introdução do método __init__

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Guilherme', 'Reis')
# p1.nome = 'Luiz'
# p1.sobrenome = 'Miranda'

p2 = Pessoa('Priscilla', 'Reis')
# p2.nome = 'Joana'
# p2.sobrenome = 'Santana'

# print(p1)
print(p1.nome)
print(p1.sobrenome)

# print(p2)
print(p2.nome)
print(p2.sobrenome)