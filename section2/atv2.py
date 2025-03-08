'''
Exercícios
Crie funções que dupliquem, tripliquem e quadruplicam
o número recebido como parãmetro.
'''

def calculando(multiplo):

    def multiplicacao(numero):
        return multiplo * numero
    
    return multiplicacao

duplica = calculando(2)
triplica = calculando(3)
quadruplica = calculando(4)

n = int(input('Digite um número: '))
print(duplica(n))
print(triplica(n))
print(quadruplica(n))



