import sys

# Generator expression, Iterables e Iterators em python

# Generator X Iterator
# O generator é uma "função que pausa", enquanto o interator é uma classe

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

lista = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# print(next(generator)) # 0
# print(next(generator)) # 1
# print(next(generator)) # 2

for n in generator:
    print(n)

# print(len(generator))

