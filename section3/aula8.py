# Métodos de classe + factories (Fábricas)
# São métodos onde "self" será "cls", ou seja, ao inves de recerber a instãncia no primeiro parãmetro, recebermos a própria classe.

class Pessoa:
    ano = 2025 # atributo de calsse

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod

    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


print(Pessoa.ano)

p1 = Pessoa('João', 25)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
# Pessoa.metodo_de_classe()
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)