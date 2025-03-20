# Decoradores com parâmetros

def fabrica_de_decoradores(a, b, c):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def inner(*args, **kwargs):
            print('Aninhada')
            res =  func(*args, **kwargs)
            return res
        return inner
    return fabrica_de_funcoes

@fabrica_de_decoradores(1, 3, 5)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores(1, 2, 3)(lambda x,y : x * y)

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

print()

multiplica_dez_mais_cinco = multiplica(10, 5)
print(multiplica_dez_mais_cinco)