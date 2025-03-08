lista = []

# Sem list comprehension
for x in range(3):
    for y in range(3):
        lista.append((x, y))

# Com list comprehension
lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

# List comprehension dentro de outra list comprehension
# lista = [
#     [(x, letra) for letra in 'Juli']
#     for x in range(3)
    
# ]

print(lista)

