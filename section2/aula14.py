def executar(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplicada(numero):
        return numero * multiplicador
    return multiplicada

# numero1 = int(input('Digite um numero: '))
# numero2 = int(input('Digite um numero: '))

# print(
#     executar(
#         lambda x, y: x + y,
#         numero1, numero2
#     ),
#     executar(soma, numero1, numero2),
#     soma(numero1, numero2)   
# )

# cria_multiplicador(2)
# duplica = executar(
#     lambda multiplicador: lambda numero: numero * multiplicador,
#     2
# )

# print(duplica(2))

print(
    executar(
        lambda *args: sum(args),
        1, 2, 3, 4
    )
)