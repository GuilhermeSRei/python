def decoradora(func):
    print('Decoradora 1')

    def inner_func(*args, **kwargs):
        print('Aninhada')
        res =  func(*args, **kwargs)
        return res
    return inner_func

@decoradora
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)

