# problema dos parãmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


lista1 = []
cliente1 = adiciona_clientes('maria', lista1)
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Claudiana', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Luciana')
adiciona_clientes('Marilene', cliente3)
print(cliente3)