# Escopo da classe e de métodos da classe

class Animal:
    # nome = 'leão'

    def __init__(self, nome):
        self.nome = nome

    variavel = 'Valor'
    print(variavel)

    def acao(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('leão')
print(leao.nome)
print(leao.acao('carne'))