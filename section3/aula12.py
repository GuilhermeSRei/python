# @property é uma propriedade do objeto, ela é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - P/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com 1 ou 2 _ (underlines) não devem ser usados

class Caneta:
    def __init__(self, cor):
        # private protected 
        self._cor = cor

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        print('PROPERTY')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        print('ESTOU NO GATTER COR TAMPA')
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        print('ESTOU NO SETTER COR TAMPA')
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Verde'
caneta.cor_tampa = 'Preta'


# getter => obter valor
print(caneta.cor)
print(caneta.cor_tampa)