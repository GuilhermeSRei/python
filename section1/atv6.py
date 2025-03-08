
# Atividade de while

#       012345678910
nome = 'Luiz Otávio'

tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[5])
contador = 0
nova_string = ''

while contador < tamanho_nome:
    letra = nome[contador]
    
    nova_string += f'*{letra}'
    contador += 1
    
nova_string += '*'
print(nova_string)
