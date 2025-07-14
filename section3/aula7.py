#__dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # self.ano_atual = 100
        

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
        
dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

# p1.nome = 'EITA'
# print(p1.nome)

# p1.__dict__['outra'] = 'EITA'
# del p1.__dict__['nome']

# print(p1.__dict__)
print(vars(p1))