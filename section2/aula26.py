# Introdução às Generator functions em Python
# generator = {n for n in range(1000)}

# def generator(n=0):
#     return 1

# print(generator(n=0))

# def generator(n=0):
#     yield 1 # Pausa a execução

#     print('Continuando...')
#     yield 2

#     print('Vou terminar..')
#     yield 3
#     print('ACABOU!!')

#     return 'Acabou' # StopInteration

# gen = generator(n=0)
# for n in gen:
#     print(n)


def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return
        
        

gen = generator(maximum=25)
for n in gen:
    print(n)