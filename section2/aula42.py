# Count é u iterador infinito (itertools)
from itertools import count

c1 = count(8, 8)
r1 = range(8, 20, 8)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print()

print('Count')
for i in c1:
    if i > 20:
        break

    print(i)

print()

print('Range')
for i in r1:
    print(i)